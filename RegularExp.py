#クリップボードから電話番号とメアドを検索する。
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{1,4}|\(\d{1,4}\)) #市外局番
    (\s|-) #区切り
    (\d{1,4}) #市内局番
    (\s|-) #区切り
    (\s{3,4}) #加入者番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #内線番号
    )''', re.VERBOSE) 

    #TODO 電子メールの正規表現を作る
emailRegetex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # ユーザー名
    @ # ＠記号
    [a-zA-Z0-9.-]+ # ドメイン名
    (\.[a-zA-Z]{2,4}) # ドット以下
    )''', re.VERBOSE)

    #TODO クリップボードのテキストを検索する
text = str(pyperclip.paste())
matches = [] #検索結果を記録
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegetex.findall(text):
    matches.append(groups[0])

    #TODO 検索結果をクリップボードに貼り付け
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました:')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした。')
