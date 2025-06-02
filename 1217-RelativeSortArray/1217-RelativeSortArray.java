// Last updated: 6/2/2025, 6:35:54 PM
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        TreeMap<Integer,Integer>map=new TreeMap<Integer,Integer>();
        for(int num:arr1)
        map.put(num,map.getOrDefault(num,0)+1);

        int index=0;
        for(int num:arr2){
            int count=map.get(num);

            while(count-->0)
            arr1[index++]=num;

            map.remove(num);
        }

        for(int key : map.keySet()){
            int value = map.get(key);
            while(value-->0)
            arr1[index++]=key;
        }
        return arr1;
    }

    }