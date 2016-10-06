from Crypto.Cipher import AES
from Crypto.Util.number import inverse
from Crypto.Hash import SHA

#rsa wiener attack
#rsa
d=945479
n=97138137104734298609834482366162026304298592110475985436506028537069205049518477940234295052306979545838532836621897425238678644632407147169000035071022811912986002484126251044062768165713546731476185662130377342101286612617162668138061510373486561911394707269228925814230274314210636439524014517539501333347
RSA_cipher=[88338041376938401802720557408228704277670863496574655328421532326725843272097398245807134173312579420393982660449469103160527683780725884286927820971842125127589841694210130213315926335981438201260031871966789654511469636565529079969394168628995175878129596748889594295059700929788081323076914856088444245112L, 61799587191566341619854870153945004198553938077225303160352458773817261402958372192378106795721702756191976223720864957706672008373655798626158938618656502841851649551320659253777035402269371424057142314225517057707462842393420846653734853164705499492891578783074253284026413294114604336927568599227641318014L]

for x in RSA_cipher:
	print hex(pow(x,d,n))[2:-1].decode('hex')

#aes
AES_key='JfffOaqYHvuSIkfU'
aes_cipher=['ciY5/kGjPdhAKVrnhNdWnrPLTRxgYyBS7qMYrz2Ak0o=\n', 'qogojMDs8nk9+xjtzaJ2as9heZ1hO4tU+lkWy5p6an0=\n', 'KFcU6TOSA9pa1rhK7z4MbB2973DWjefjdtLpAL3e7j2kyKh958JjDgs4gP+z14Fu7C6u40ol/t2d\nm5MVgeY93g==\n', 'EmS6a94W5adYv6t4lClWso8eBEc43Bv6UDf2di1eaS40jPfkKhplW2xZqhftGQSQxbXPRo7pkI7e\nItzc0WCy0P8TT49/UPAMF5b60gDZMPt2j/ZRAuHxaJzF8Cx2it7gKs24ncfTd4SOWe2u7MKOKw==\n']
for x in aes_cipher:
	aes=AES.new(AES_key, AES.MODE_CBC,x[:16])
	print aes.decrypt(x.decode('base64'))[16:]

#elgamal
y=15148966177463904691976929838930853269289042839863729153722159418042428750060107430271482040640819799571694807206565563732947531693110647584022938487969095426383780089637260478432928271983711941845660111527182345478689092328947780732610986992284917052181103606943301549620374333055713772173803160039045677747L
g=25986687973107588697969881578531976225371183716036966607566598597020466205189059529253570979189706405467377222766170735056450913652725357600357578278196605120029525929914741729624555676312392184452733004866834101377570297318905377030568966047530761331315780489316379915546238079764422405334804304898426687980L
p=137967888557999584952319237542893026336748210577336880254687758603509585370528901731055615450121641462482424970657347865301939510121259558782471038671268295347199943208985837721430708786848240150088389965993410045395623590020110797728504435013202372429725107610844546670040670171936933047396461805698152157887L
a=39370371870759685744880219013861529359618555030410863001040308371947410012054549207612071728536023322186748226046661353393772853562380526414095218658206970877514669689306990840319762479981191161383790605961521206224285819589569439347118291570125764824252249717974718794796429000637269474821559491639876277622L

b_1=134684485624161722987021635696340906125874242700255840489978717909572949629047583933623167185071756551222666372564819181853883708840908663577036374636521884329720103037550136452569114301719473556970058712470208671611709476886062032130414621155592035982216482184069779157329196503823026688539159075884112435996L
b_2=105396166206430883198614275890827062056159012286110042575572024146834036632816276753821090982097827834427186711544957971715438182849629129341938574550891409300133967462947765862253827035010131907704291025456105903654968880992395975177059676410502095248239091847873470990731624808614783122403783791697356313395L

m1='ESIGN'
m2='in these Signatures, important things r different....but....they r one and the same. indeed.'

h1= int(SHA.new(m1).digest().encode('hex'),16)
h2= int(SHA.new(m2).digest().encode('hex'),16)

k = (h1-h2)*inverse((b_1 - b_2), (p-1)) %(p-1)
##secret key in elgamal
x = ((h1 - k*b_1)*inverse(a, (p-1))%(p-1))/2##--------------->or :  x ==((h1 - k*b_1)*inverse(a, (p-1))%(p-1)) + (p-1)   

print 'elgamal secrect key:>>'+str(x)

tmp=''

aes_cipher=['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\nCoMBVWdOfxPXhsInNAm5h3G7XqM=\n', 'ph8RjRg+OQcHinhv2aVqb6eRuwK06y1jy1SeVnMFCVcyhuhC+Q1atNTe6GmMR415ZLXBOusFUaQR\nKgWB/5QQ8jG1yccPqHJ1VA+xkjtyt92tc9TJL6iN74pNTECd8yQ4r4CuKkG7t4qbT7HByD5mxVPn\nw3uxiOes4pjGUgF8Y3BKwubiDuhOahYSK1lYdlvsTBbnVKjzUBX4OySXNg4Tg/gdFVWvxbYPE0Oz\ntbKD+THwgfEUmpF8V3VY8ogAi4e+tWrru3BYdEtj9QBmmRAqaAPs9IvXUiER/CEgxtaj9W3cAO04\naa6DCkCA0ZXqsJQB1ZHpHAIb+wMXWODJzYSoHOB81HfmTVzkIxd71e891iACnSo/f8r0YOdDN8JR\n9r728+CMKlAXOdhKcnmS9nPPCZw87UROGVK4hNuNpggJ0tdHkgOcLAJqK1cMxbBHXPiyZF675EL+\nprgn6pQWhVS2ckLLroG4RrIoKs4E0oO7ibPtbFZmbsz1mE5h3D5Efo82Ry5Jd1e246tBKHrqIUL2\nw9TwGMHZhTVND/bY0ONsAIASZMiJwOQPl7ejsu544QwL7estgePpGGITbuPZvt+2vbmIcbz3GG/W\n5qmHYK4EcpfHJcRxwkeu2wlH3IjxaSJj+aeYM0u9Ne0JaaIhzFquTFp0CaEYCUB2nBv9IodKvlUr\nNTKTu5/TlTQxa3cdVzKr1wnAjzpQ5gGq/47jjZN6E63aemJpJFrvGTpkiaCNUIMgSV5GqvCETROy\nXWKun5G2fZFS4nYnph4NUHLMNMpf4wRgd6V15G0dy6c8ngPqu/oWW/heynguUnN0pC9UIIVNo5RX\nuiyejhEab3LtnVglF0Hyj5d2xrcJJY9GvykN5H1Qq5ekvtYyf1ABFh9lw9PbkIK21ExOvIQqSSKf\nr58Oe4LwO819zmWq1EJZaIjIVUAwOGdOgjjVthBLDQ5nLkfC8LsCaYVDFY2VpbIAPFEB+LGOSRPg\nhtcYZqc3m0lJ6wo=\n', 'GRjhnUU1+q08d6/e0aU5AwQIBcFMLyGyIL39Gt92MbgQyNbcYOJMAPQ3RJp6LGKeE9HKUpOLsSlr\nh06NAL350RzJLhJwcaKDq1cEkN65acy0nwabltQp/U9RUNkY/djQEYpEYWFgMet1j8gdre7RMc4Q\nC/08MmLcRwHSwmr5OnJKc3KbFUksGV15ERlNDTG3INTjE2w1ZepBA3G4BNz5AMa0/yLOTZvcZH0z\nXfsCmM32kfH11w3MowrPcRdZkpdbsKZVpmKWO1bntg/pozGxJlbYXK6t4gJhWzZM29xiBxpVCUMT\nBd4MpTRLKitvL6AMN6EJLMRfBZn5idu/zCEwv/VeX+3Ibq/SAFzaaDohUd8Z6t4w+mX6QLOPoiDL\niVgITCPkDQvkSZYXQlZaSW/LqGP0pJN9YIReezG8mFyo9YyNjr+Zkxp7RkDeXq7FVaH+L2nhqpSP\niIl1tCR6yOuLomI0xnK2seLYRekEYYJY0E9+Ym+2HsnTBQSVGedc3P1u70UsBlQXj1/2JKBduUDf\nlOERaW4f+qnDEZliSL91Jeo=\n', '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\nMNkPLXbITHALf1CIqQf0xBNEm7jlOvcYDWzD\n', 'DUEHkcLhWgLOaRmLyZ/ir1ZRJ5J/PI8ekzWJpam0Rk1mZ0t7YD7y7gASHLEuspzrWfZQLeIlAX/W\nQVVdDKwsCF3pfFn3z4hBxP2IfFAbuvdNETEjhIKtHFE/czUpFH6OvHlWkuHI9mq6Kf5X4LCTQwqW\nAvlIgz7valMYudCTiUUt3aiYYlJFO6uCg03GjnKehK5/cPA2QACI24GAo2uPVII0SnygAehNw/AG\n9ZBCE3r9ZF/qP7RAdfQPZw+wUFiFwAAMQNU87ykTFn0v2Xbfj0Rp313+6yubjNkMAmB6SzkbInUM\nb/DoCHYZwHfFn4WbNycN4IJI/d2OIOVwlUyZU5tlgMxQQKK/IHS3AKTfuIWAXoal8oWG61mqzpaU\nZ2ZctqfFfaA/0eoq1SQYnnD9TCfIsWiZoOsvVBeb674YrY6epGRCbOuWPGnyFK0EPCk6ZZZ4GZH2\nse5Pvyr6vbn3qFtop7jCehSobYLS9i2IHuM5TGPJYkpIehuXbPM8IZ8+rMc7j1Ypt9Gapj6wqUN0\nLXCZgpoBRo89GXNRHrHpdLcyk8IF/q8L8/ucze/QZMKvM1UPOf2U9jqNFipf9RCFyQ3CxEfII488\n/q6EHN6rapczWQl8alQrmY8P5oSiJic6KlD18cDS9NIPdGajxg+rr9H7sQlZBVD5ILaAb7Okwnsp\nL64YlIAvEyO+sknsW4BLHD3wH0HgmoGmQoYSfz94wA==\n', 'lxmbvU5gPSomqdQ2ADwPl42v5gY0pmcNYNbnTf4jnvbIf4aPYBm84hI4T40kKJ1JmapldCP/Xdtg\nRXi75G8mdhBKq42sy+f71T7sAI7yIIwbY7HOly98E5OgkYlMl4uhsXXMgFTCZY9sfFxesNlBNP9N\nYjy7L2qh+vzx41WF8vMBJm0Q+IlTJ3WqOCnt2y3kBPjpfv2kY2DMuq7SS2l/hMA44GcsM+aRo9PX\n/pdn+OcBnOhz7Q1eZ8g2YnJff3oM4a9Ch5zuIbWvR/ku4eGCAXBnoJZuAUJ4to8hIda+CD4ZniQY\n0IxJty1ml+fB9j1jrzmiCTlET9145dgV1xKjkqQplHpgOnELda3H93giULgwMR33TfRu9VICJlqD\nhwTIGEGOwSI8x6zoJl29zEOrqUqdxuvRUHc/lrmBPYjDnoWeVVN00Tv+VhL7oac62WBLCtybNQKz\nSPcQufg355gWAxyYjFvi9q96jlVTm9G+7Sbt/K7iNqhqEObW2ftgkR60W2FmJ85W0Ea+4CDuG9hJ\noRrpCJ4f/pGEJf9zBZjuPZ1rtQA6HLZg55Ngo0xSfE3+qZF+4PW97Oq8vohgu8m150QUoAXzC9ET\nzT/YjuRP3LEEVkiw/+f7DQBPr99atB0kp1ZvDPN4jv1z+mSgqo1PTjqvXYGy3d5SiFE3r3bI11Qk\n4GMLV3fEhwY8r07mor95Ib91UESke+PfAkF8njB5vUoI+1E1gw9x84Lm8T2NInYYhsYtnPnc21Jy\nYrchJJddZ8o/kYMD2Yk401mRu/4I99nJb+CCcLQJRYjqca1B3Fts2Kc4yAFCWsCEyNBglWv0EnHT\nATFRHy97y0JS0YRFsolksigZKkZMTHylxe+Lz/WRjhgLhrMZS2Px0uFzJfr3L23iJ7VJ8uxpPlAD\nBAkOkLOsNfHmtjZM2TVX9gjH1SwFH+5+oAy4TnkjtrvSeqIBcloXJCcwr/PoxPbjPLlZCbCd4Uaw\nzeRjP2cCeJ3sKd3pYFlnruDYNophDRpQKu5W2MyD1P23DfemtrGn4V1j/uSIfZjmaRI0HKIomcs0\n6BcYZBM7FrnVsHBT8kiCHEmhr3kzJ9MwXgRdzX/dKgIUyPRlmOVX0RuGg+RBHMIg8RcgamtPtnz8\n8G5GyeCe+E0U\n', 'vJ9r9C4RduBDWIJPJkEQn/+DJd7fsmyKPdNG1ky2+w8ukb3b7hINOOFTR8G8dyCOqD/39hOh9t8l\nXc2St+PEeCNLrq7+PLbYbIuDPoTHv9EaOouiZqugj2esWkLDQrnDcXtNqtlS+5Fuez8YdWaTwbmk\nHSJKh2fIED/m3Zb06KnQGUQqzhTbcLMvtjGOh+L2mBaNqbyxYMizDx+Gf7s+uj2SKDMd+qdzGd+n\nSCHg0mVfP0l7bYwDEeZjpwoCK0RkxahNAvQkrplrcafdgePvoO7hBrwXZXU8etsEb0NdvBTQWI+R\n2DbJcr3zAwWFkG3GrTl2TPvaw/vLAyFM6PFyh9VzdztYVi4aF0ZS49q3riFngIqhW1RkVeUy/i3/\nToLehtzpZwedHkcpL53hSHAE/ZzeqRI4fVvV4ZSGbAzuipa8fFhnbV9c+Jlm0p6fHY9nR+aUVQx6\ntQ+z8EsP3Jazbko2NMLVqAVQr6Jht/a2vW+xKyTD0B1CGXqOTu1qdaTJj0+5TYn7BljWSnhUWzTd\nru4OnCuNttYVVn9H201TsltTry2uZzDdBbTchaZkSoPU0UFNQvnIoG3VLFD8mQYMxqHv0UXxQE/f\nmnkUCjtI3S9YoOKYVWjOXklDjJKX349E8gONr0v9shF6Y6xgJiavOe81Qjn/2tZzKgy6b55084n4\nlcX22uifOjWwGQTLXYwNnZYUkyt9+mvzphLmfCr20g/bksNxxVGRiJ7BEAZUbQ0gUkEcMMcCbF6K\nkYCvqqJxsuYyR211YK5BburdM8ixTrtnbOSgAO1tSv2IysU5PgIoRA3sXfku5hVdihWh70Ppdq1o\nTPsPgE1/zEHJjEseIiKezsqHCDqvyzMsyhjqrmYuBFQ5H7dmLl1NSigy76sEMP21z7i6Nx+iwOen\nJDasRZbKRZyE0jZE2qKTnnTmq9rpXx4dEKg1gV0JYv9f0ARaOjJhHINXIaM/ruz7ujKHeTjCptEW\nU6oy7dSQKu3hkLmvoxAY/m5uyMwP42j5a7JRuPmKjzVpoqQX6JUwBfjxX9+kCAaUZv+hmqcQJ7nU\nRyPihABajrffN4ccpgKOGWHG2mmH+DRnQis5H3vByLu7dEk9oXgop9zmz1Cz2kEYNTgZLTht6lGa\n1Jk6j9nbYKP4ca2tU23d7l1llGU3XddQQw==\n', '7QpydF/gtKINERN/KQsVMPgcHFBT4UcZGzc+rbbhzluDA26+T1f0wXzo/o3D8bHGaDNi8dSD1/HP\nsayjyiVlN9Dl3IeMhszEUle/hQN3o1rEBXb9pNt7POfoMNO/KjK9Dx6E597Mk5ge6HqJKw34OMrL\nHgpl8aD99nVk04GTdE55W7mFNvKWSGpGyq2eo9GlMWz2d9y4oAHB9d74ukqMAmvBN0jwuBnzFNPE\n/H0R7ZZAys9RhGxI9Ul21BeGAfZwIcS0WRadbcgxEduEcySiuccbxkMaTd45WXd+OjZ0A/7AnV16\ngls8tLFN1a0K7VrbnjgyG1gqiz0KbCofVMal/x0rAN8Mvy9F4CWrU496Kl5BQTgdkkciZDzHzqkx\nikWtHRHivaZxJsvv5OzE5dvvkRP3dpM0ciJ2hyPabfCNTGNe+AuFuDdhvf+Z3ETkZR36K/UZguju\n4ZvoNKxhLq6v44YklUNJ6rplY8DWsUUxe3m/AbPUb/mKbJ1ddOKSao8IiNtHgOQMe2ec5hnaY6Om\nFGQarjR8qYS8W89PPAlmRYe6ifejDCbP3xWBf6XxgEw8JOM0D4pdn7fpLH1Mdf0N5JVXG20fYENs\nUsilIIVmF9PbBBeuZNtvTjYPfaGMdW7dmCgwpBk8gIfJoBGw6AHLPIRvbn2c56jywvP8RPuFkxgX\njxbHjkkHTRevRuBBFo9sSahSyE0qR/iOhsURfxC3Q74hj3qimIdAd7nqCXUi7J3WX2A5gUr1rpCI\nRKy0zNvPiSHDB9MWTQ8BAO0nnQaBld/5Se99IK2omFnOig2tt6/USM/MN/eeY1K/BVe0SPp0VnFA\n716T/A++ayDV/3esqKu/bXV3r56XmBFDGAqiAyCPH+Pu8t7WUzQXckuJn9X7Psc0vQDOck61k4Hq\nUNIdUWX6WQPQ3mhAXa8FlAcLIYWv1/H7SCTXF005Sb69yxbUxCC6FIIN9xx5kvj1pmT8DbWHFwhG\njwmgJinW6dJ1E5hh1Awfd7/CZPcW5/7RBCifdBMZXyVfPbh/bFLBCaQqONA09C8IbalLSxbl9qD0\nN8iD5NmFGXT8qfYR/PITFiOdbLNO6xlcRBf/Kn19CSD1VEyRND4MXYvjjIQ3rHCsdCtCMRImYkXL\nFakZ0mU2uhFRZlOymb7gCuhS8cQVw9SDDmb25Y9fIJ3QHqazTgxz7kLyb519Bf1ZE5ygclU4vzWY\nde2jQ/UHaq5pyqjg8Jd/epZ2BeQP9Z4WMps5gAHwmFfcK5WDwI7HT3eg7bebo1+yX2U8FRzxc5EQ\ncOiw0artxnSbG/n6j32eMRtF5W3pov4korSghlYGSjf/eGueDJbW6T4+SeGLRdgles0yrkEN6K1M\nx5qcn0bsBL4irfT00IMo3m6DRiHwIUSnxBLeQPEnDNH0LMbg5xU1E3I4C7CX4cJGRB+LNyrx/kbf\nrAw0CoI8XRBx/2IINBsuK/j4OP3V\n']
for each in aes_cipher:
	aes=AES.new(AES_key, AES.MODE_CBC,each[:16])
	print aes.decrypt(each.decode('base64'))[16:]

esign=[47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177114900132904208031268302055034139561094L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177043126968026032278260335612769217465281L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177048437820735552471626935982805579762300L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177021833404976799204855378090578793909689L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177047077353854576295462347808999410606732L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177109317561681513876512377036078526549896L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177046828309551946677942463028497367867022L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177054808825693181779307343835312685224642L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177108259205278901023354961482837418958536L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177118898318679253860822585787041787977907L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177036512413482804011903184399450788697718L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177114900132898945572068297162714907204040L, 47151187630170508946550590940497421816323570626342529264695210340018989341227979713866943813866053413150335084934817107617993172782066024755642911882059190347569889101139210027601350765558686021652374574364157734035825031651335006681991745326523882879567488679550114398601894015152212989669287744229828109313772135492989363845359569577930002703168580012177024614659746333751944013277918979979452838910451314830517626226812111086617001446819759278727669699433710723965740498925499287801336151510037755053019684620660717114330472099865458814571094207720509115863001849254027733865594330714620127867103989520820147652839911441693648565908877821604091210108678987867242564251709096595005423318352932402719925534847930784847299511987496721904066523578263274498793322917788336595457279846976363887848066280738155134219879078067684956409012070198076296654028153831098694860754975328932529207057974618110712280934666664728972656076484522040533059678936174289345253777045003597312000627579157387613037538709979271187902698911832876797141724749720913114489026277701176857072667073091116052491281774213875710421731415977953374297574181411476522002777637311080653697834289305316477478889515245281489854177021915162579455595532972926008542466995L]
for e in esign:
	tmp += hex((e%x))[2:-1].decode('hex')
print tmp

