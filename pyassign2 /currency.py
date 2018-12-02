def exchange(currency_from, currency_to, amount_from):  
    #定义函数 currency_from为输入的已有的货币类型，用三位大写英文字母表示的 currency_to为想转化的货币类型#
            #amount_from为想转化的货币个数#

    from urllib.request import urlopen 
    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+
                  currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return (jstr)  #输出的jstr为string类型#

def live(jstr): #该函数为将上述jstr转化为字典，并判断输入是否有误#
    import json
    jstr = json.loads(jstr) #该函数为将str转化为dict#
    to = jstr['to']
    if jstr['success'] ==False: #判断函数输入时是否有误#
        return('出错了QAQ，错误类别为'+jstr['error'])
    else:
        return(love(to))
           
def love(to): #该函数是将‘2.333 USD’转化为2.333浮点型#
    num = ''
    for eachChar in to: #遍历字符串to#
        if eachChar in '1234567890.':
            num = num + eachChar
    return(float(num))


        
def test_love(): #测试love#
    assert(love('2.3333 dollars') == 2.3333)


def test_live(): #由于live和love绑定，就一起测试#
    assert(live('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros",\
                  "success" : true, "error" : "" }') == 2.24075 )

def test_exchange():#测试exchange，但是虽然很长但不能换行，用\会报错，不知道为什么#
    assert(exchange('USD','EUR','2.5') ==
           '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')

def test_error1(): #测试输错情况#
    assert(live(exchange('xxx','USD','123')) ==
           '出错了QAQ，错误类别为Source currency code is invalid.')
    
def test_error2(): #同上#
        assert(live(exchange('USD','xxx','123')) ==
           '出错了QAQ，错误类别为Exchange currency code is invalid.')
        
def testAll(): #全部测试#
    test_love()
    test_live()
    test_exchange()
    test_error1()
    test_error2()
    print('All tests passed')

if __name__ == '__main__':
    testAll()

currency_from = str(input('请输入你已有的货币类型（要用三位大写英文字母的缩写代替哦）：'))
currency_to = str(input('请输入你想转化的货币类型（同上）：'))
amount_from = str(input('请输入你想转化的货币个数：'))
result = exchange(currency_from, currency_to, amount_from)
result = live(result)
print(result)
