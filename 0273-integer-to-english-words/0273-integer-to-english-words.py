class Solution:
    def numberToWords(self, num: int) -> str:
        def subwords(s):
            n=len(s)
            one=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
            ten=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
            ones=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
            res=""
            for i in range(len(s)):
                if n==3:
                    if s[i]!='0':
                        res+=one[int(s[i])-1]+" "+"Hundred "
                elif n==2:
                    if s[i]=='0':
                        pass
                    elif s[i]=='1':
                        res+=ones[int(s[i+1])]
                        return res
                    else:
                        res+=ten[int(s[i])-2]+" "
                else:
                    if s[i]!='0':
                        res+=one[int(s[i])-1]
                n-=1
            return res
        
        if num==0:
            return "Zero"
        l=[]
        tem=""
        while num!=0:
            rem=num%10
            tem=str(rem)+tem
            num//=10
            if len(tem)==3:
                l.append(tem)
                tem=""
        if tem!="":
            l.append(tem)
        
        res=""
        tens=["","Thousand","Million","Billion"]
        n=len(l)-1
        for i in range(len(l)-1,-1,-1):
            sub=subwords(l[i])
            sub=sub.strip()
            if sub!="":
                res+=sub+" "+tens[i]+" "
        
        res=res.strip()
    
        return res     