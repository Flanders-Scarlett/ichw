##1.图灵为什么要证明停机问题, 其证明方法和数学原理是什么？  
因为图灵为了证明希尔伯特的可判定性问题而提出停机问题并证明的，证明方法为对角线方法，数学原理为反证法，假定可以判断是否停机并引出悖论，
故判断无法判断是否停机。  
##2.解释二进制补码的原理。  
假设中学生知道二进制，为了表示正负，我们认为的增加第一位代表符号，1代表负，0代表正，又为了计算机计算方便，我们采用反码的形式表示负数，
然后因为这样会产生+0和-0两个零，所以我们让负数的反码统一加上1，即在原数上统一减去1，从而使-0代表-1，这样就解决了两个0的问题了。  
##3.某基于 IEEE 754浮点数格式的 16 bit 浮点数表示, 有 8 个小数位, 请给出 ±0, ±1.0, 最大非规范化数, 最小非规范化数, 最小规范化浮点
数, 最大规范化浮点数, ±∞, NaN 的二进制表示  
+0：0 0000000 00000000  
-0：1 0000000 00000000  
+1.0：0 0111111 00000000  
-1.0：1 0111111 00000000  
（绝对值）最大非规范化数：* 0000000 11111111  
（绝对值）最小非规范化数：* 0000000 00000001  
（绝对值）最大规范化数：* 0111111 11111111  
（绝对值）最小规范化数：* 0000001 00000000  
±∞：* 1111111 00000000  
NaN：* 1111111 non zero  
我不会排版orz。。。
