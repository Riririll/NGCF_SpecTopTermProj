# Neural Graph Collaborative Filtering
This is our Tensorflow implementation for the paper:

>Xiang Wang, Xiangnan He, Meng Wang, Fuli Feng, and Tat-Seng Chua (2019). Neural Graph Collaborative Filtering, [Paper in ACM DL](https://dl.acm.org/citation.cfm?doid=3331184.3331267) or [Paper in arXiv](https://arxiv.org/abs/1905.08108). In SIGIR'19, Paris, France, July 21-25, 2019.

Author: Dr. Xiang Wang (xiangwang at u.nus.edu)

## Citation 
```
@inproceedings{NGCF19,
  author    = {Xiang Wang and
               Xiangnan He and
               Meng Wang and
               Fuli Feng and
               Tat{-}Seng Chua},
  title     = {Neural Graph Collaborative Filtering},
  booktitle = {Proceedings of the 42nd International {ACM} {SIGIR} Conference on
               Research and Development in Information Retrieval, {SIGIR} 2019, Paris,
               France, July 21-25, 2019.},
  pages     = {165--174},
  year      = {2019},
}
```
Example to Run the Codes
``` py
!python NGCF.py \
    --dataset amazon-book-small \
    --regs [1e-5] \
    --embed_size 8 \
    --layer_size [64,64,64] \
    --lr 0.0005 \
    --save_flag 1 \
    --pretrain 0 \
    --batch_size 1024 \
    --epoch 200 \
    --verbose 50 \
    --node_dropout [0.1] \
    --mess_dropout [0.1,0.1,0.1]
```

## Dataset
We provide two processed datasets: Gowalla and Amazon-book.
* `train.txt`
  * Train file.
  * Each line is a user with her/his positive interactions with items: userID\t a list of itemID\n.

* `test.txt`
  * Test file (positive instances).
  * Each line is a user with her/his positive interactions with items: userID\t a list of itemID\n.
  * Note that here we treat all unobserved interactions as the negative instances when reporting performance.
  
* `user_list.txt`
  * User file.
  * Each line is a triplet (org_id, remap_id) for one user, where org_id and remap_id represent the ID of the user in the original and our datasets, respectively.
  
* `item_list.txt`
  * Item file.
  * Each line is a triplet (org_id, remap_id) for one item, where org_id and remap_id represent the ID of the item in the original and our datasets, respectively.
