首先，要想理解cache，先理解内存。内存的简单表示如下图，内存里面的内容的查找是根据地址来进行的，也就是说内存包含两点①地址②内存的内容（存的数据），根据地址来找数据。  
![图1](https://raw.githubusercontent.com/Flanders-Scarlett/ichw/master/TIM%E6%88%AA%E5%9B%BE20181008103641.png)


                                           图1  内存的结构

   上图的0000-0008是地址，A-I是存的数据，cpu根据地址去寻找数据。图中的一个字母代表一个字节的数据。    

 我们都清楚，cache中的数据就是物理内存中的数据的子集，那么对于物理内存的一个数据，根据cache中可以放置这个数据个位置可以容纳这个数据，则为直接映射的cache；②如果cache中有多个地方可以放置这个数据，它就是组相联的cache；③如果cache中的任何地方都可以放置这个数据，那么它就是全相连的cache；如下图2所示： 
    
    
![图2](https://pic3.zhimg.com/80/v2-7d6ae0a0629fddd89d947ee5567d075e_hd.jpg)


                                           图2  cache的三种组成方式

   更详细的讲，cache的结构其实和内存的结构类似，也包含地址和内容，只是cache的内容除了存的数据（data）之外，还包含存的数据的物理内存的地址信息（tag），因为CPU发出的寻址信息都是针对物理内存发出的，所以cache中除了要保存数据信息之外，还要保存数据对应的地址，这样才能在cache中根据物理内存的地址信息查找物理内存中对应的数据。（当然为了加快寻找速度，cache中一般还包含一个有效位（valid），用来标记这个cache line是否保存着有效的数据）。一个tag和它对应的数据组成的一行称为一个cache line。如下图所示，下表中的一行就是一个cache line。
    
    
![图3](https://github.com/Flanders-Scarlett/ichw/blob/master/TIM%E6%88%AA%E5%9B%BE20181008103659.png?raw=true)


                                           图3   cache的基本结构

具体的Data、Valid、Tag各有多大，在介绍了内存的地址划分之后再在下文中讲。

知道了cache的结构之后，如何在cache中去寻找对应的数据呢？简单起见，我们先选择 直接映射的cache组成方式进行下文的分析。

首先对于一段物理内存（block），该物理内存上的每个字节的地址划分为以下几段：[3]
![图4](https://github.com/Flanders-Scarlett/ichw/blob/master/TIM%E6%88%AA%E5%9B%BE20181008103706.png?raw=true)


                                           图4   处理器物理内存地址的划分

这样的话物理内存中的数据到cache的映射关系如下图5所示：
![图5](https://github.com/Flanders-Scarlett/ichw/blob/master/TIM%E6%88%AA%E5%9B%BE20181008103718.png?raw=true)


                                           图5  cache的查找过程

   上图的映射原则就是：根据物理地址的中间三位（index字段）来定位当前数据应该在cache的哪一行，把物理地址的tag字段和该地址对应的内容放入对应的cache line的tag字段和data字段，并把相应的valid位置1。那么在之后进行cache寻找的时候就可以根据cache line的tag字段来辨认当前line中的数据是数据哪个block的。

   上图5中的地址00 000 00~11 111 11按照图4的原则进行地址划分：地址的最高两位为Tag字段；中间三位为index字段；最低两位为Block Offset 字段；由于Block Offset是两位，也就是一个block的大小是2²=4个字节的数据，也就是一个cache line的data字段包含4个字节的数据；index为3位，说明cache共包含2³=8个组（对于直接映射的cache，也称为8个行）；很明显，cache的一个行中只能存储1 块(Block )=4字节的数据，但是按照图5的映射方式，会有2^(tag位数) = 2^2 = 4块的数映射到同一个行，此时通过Tag字段的比较来辨别是不是我们要取数据的地址，如果不是的话，也就是发生了cache的缺失。如图5的Block 0和Block 1的index字段都是000，按照上面的理论它们都应该映射到第 000=0行（这儿的行也就是组，因为图5是直接映射的cache），但是现在第0行的内容是K、L、M、N，也就是Block 1的内容，为什么呢？仔细看该cache line的tag=01，映射到第0行的块只有Block 1的tag字段=01，所以可以得知此时该cache line中存储的数据是Block 1的数据，此时如果CPU发出的访存请求是访问Block 0 的话，也就是发生了缺失。此时进一步定量分析的话，共有4个数据块竞争使用cache 第0行的位置，也就是说cache的命中率为25%。

   上面的过程总结起来就是：物理内存的索引字段(Index)选择cache 的行，通过对比物理内存和cache line的Tag来判断是否命中。块偏移字段(Block Offset)可以从cache line的数据块中选择期望数据。注意在这个过程中cache的index是不占空间的，它就类似于物理内存的地址，对于物理内存来说是通过地址去寻找数据，对于cache来说，是通过index来找到对应的cache line，或者更通俗的讲就是：cache line的地址对应的就是物理内存的index字段。

   此时该cache的容量计算如下：每一个cache line的数据字段占4个字节，共2³=8行，所以数据占据4×8=32个字节，一个cache line中tag字段和valid位占2+1=3bit，整个cache的tag+valid=3bit×8行=24bit=3Byte，通常情况下我们都是一cache中数据部分占的空间表示cache的容量，也就是32字节，但是实际上，它还额外多占用了3字节的存储空间[4]。

 

   图5的分析是针对直接映射的cache进行的，对于组相联或者全相连的cache的分析与之类似。如果是组相连的cache，每个组(set)里面包含多个行(line)，通过内存地址的index字段来寻址组，确定组之后再根据tag来确定是否命中；对于全相连的cache，就不需要index字段了，因为全相连的cache相当于只有一个组的组相连cache。这是只需要根据要寻址的地址的tag来逐一与cache中的tag字段比较，如果有与之匹配的cache line，也就是cache hit了，如果遍历整个cache，也没有找到匹配的cache line，那就是cache miss了。

 

注：为了叙述的简单性，省略了内存地址通过TLB的的虚实转换部分，由[1]可知，内存地址的Tag部分其实是需要先经过TLB的转化才能够去和cache line的tag部分去进行匹配的。
