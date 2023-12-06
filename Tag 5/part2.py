import multiprocessing
import signal
import sys
import time

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.6+
    count = len(it)
    start = time.time()
    def show(j):
        x = int(size*j/count)
        remaining = ((time.time() - start) / j) * (count - j)
        
        mins, sec = divmod(remaining, 60)
        time_str = f"{int(mins):02}:{sec:05.2f}"
        
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)
        
    for i, item in enumerate(it):
        yield (i,item)
        show(i+1)
    print("\n", flush=True, file=out)

def map_value(maps,value):
    for map in maps:
        if value >= map["source_range_start"] and value <= map["source_range_start"]+map["range_length"]:
            return(map["destination_range_start"]-map["source_range_start"]+value)
    return value
# @lru_cache(maxsize=None)
def get_location_value(map,seed):
    # if seed in cache:
    #     return cache[seed]
    soil        = map_value(map["seed-to-soil"],seed)
    fertilizer  = map_value(map["soil-to-fertilizer"],soil)
    water       = map_value(map["fertilizer-to-water"],fertilizer)
    light       = map_value(map["water-to-light"],water)
    temperature = map_value(map["light-to-temperature"],light)
    humidity    = map_value(map["temperature-to-humidity"],temperature)
    location    = map_value(map["humidity-to-location"],humidity)
    # cache[seed] = location
    return location

def get_lowest_location_for_seedrange(map,seedstart, seedend,Queue):
    location_values=[]
    for i,s in enumerate(range(seedstart, seedend)):
        location_values.append(get_location_value(map,s))
    Queue.put(min(location_values))
    return min(location_values)
    #return min([get_location_value(map,x) for x in range(seedstart, seedend)])


def signal_handler(sig, frame):
    # with open("save.pkl","wb") as savestate:
    #     pickle.dump(cache,savestate)
    sys.exit(0)


if __name__ == '__main__':
    f = open("Input.txt", "r")
    # with open("save.pkl","rb") as savestate:
    #     cache = pickle.load(savestate)


    current_category=""
    almanac= {}
    seeds = {}
    for l in f:
        if len(l) <= 1:
            continue
        if "seeds" in l:
            name, seed = l.split(":")
            seedarray = seed.split()        
        elif "map" in l:
            name, map=l.split()
            current_category=name
            almanac[current_category] = []
        else:
            destination_range_start,source_range_start,range_length = l.split()
            almanac[current_category].append({
                "destination_range_start": int(destination_range_start),
                "source_range_start": int(source_range_start),
                "range_length": int(range_length)
            })



    lowest_locations = []
    threads = []
    queues = []
    chunksize = 500000

    signal.signal(signal.SIGINT, signal_handler)
    # with concurrent.futures.ProcessPoolExecutor(max_workers=16) as pool:
    for i,s in enumerate(seedarray):
            #print(s)
            if i%2==1:
                continue
            range_start = int(seedarray[i])
            range_end = int(seedarray[i])+int(seedarray[i+1])


            while range_end-range_start >= chunksize:
                queue = multiprocessing.Queue()
                p = multiprocessing.Process(target=get_lowest_location_for_seedrange, args=(almanac,range_start,range_start+chunksize,queue))
                range_start+=chunksize
                #print("Chunkstart",range_start,"end", range_end,"remaining",range_end-range_start)
                threads.append(p)
                queues.append(queue)
                p.start()
            queue = multiprocessing.Queue()
            p = multiprocessing.Process(target=get_lowest_location_for_seedrange, args=(almanac,range_start,range_end,queue))
            threads.append(p)
            queues.append(queue)
            p.start()
            # while range_end-range_start >= chunksize:
            #     threads.append(pool.submit(get_lowest_location_for_seedrange,almanac,range_start,range_start+chunksize))
            #     range_start-=chunksize
            #threads.append(pool.submit(get_lowest_location_for_seedrange,almanac,range_start,range_end))
            # lowest_locations.append(get_lowest_location_for_seedrange(almanac,range_start,range_end))
            # with open("save.pkl","wb") as savestate:
            #     pickle.dump(cache,savestate)
        
        #pool.shutdown(wait=True)
            for t in threads:
                t.join()
    for q in queues:
        lowest_locations.append(q.get())
    print(min(lowest_locations))