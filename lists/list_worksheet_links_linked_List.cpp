list1 = [Rand_len];  // List1 of random length, with random values 
list2 = [Rand_len2]; // List2 of random length, with random values 
list3 = []; //Empty List
list1_p = 0;
list2_p = 0;
for(i = 0; i<len(list1); i++){
  if(list1[list1_p] < list2[list2_p]){
    list3.append(list1[list1_p]);
    list1_p = list1_p + 1;
    if(list1_p = len(list1)){
      for(t = list2_p; t<len(list2); t++){
        list3.append(list2[t])
      }
      break;
    }
  }
  else(){
    list3.append(list2[list2_p]);
    list2_p =list2_p + 1;
    if(list2_p = len(list2)){
     for(t = list1_p; t<len(list1); t++){
        list3.append(list1[t])
      }
      break;
    }
  }
}
