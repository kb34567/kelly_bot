from transitions.extensions import GraphMachine
import requests
import re
from bs4 import BeautifulSoup
import telegram

ROOT = "http://www.atmovies.com.tw/"
CAST = "http://app2.atmovies.com.tw/film/cast/"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_garbage(self, update):
        text = update.message.text
        return text.lower() !=  ('1' and '2' and '3' and '4' and '5' and '6')

    def on_enter_garbage(self, update):
        custom_keyboard = [['台北','台中','彰化'],['嘉義','台南','高雄']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("輸入你要哪個地區的電影 1.台北 2.台中 3.彰化 4.嘉義 5.台南 6.高雄",
                                    reply_markup=reply_markup)
        update.message.text="-1"
        self.go_back(update)

    def is_going_to_state1(self, update):
        text = update.message.text
        if(text == '台北'):
            return text.lower() == ('台北')
        if (text == '1'):
            return text.lower() == ('1')

    def is_going_to_state2(self, update):
        text = update.message.text
        if(text == '台中'):
            return text.lower() == ('台中')
        if (text == '2'):
            return text.lower() == ('2')

    def is_going_to_state3(self, update):
        text = update.message.text
        if(text == '彰化'):
            return text.lower() == ('彰化')
        if (text == '3'):
            return text.lower() == ('3')

    def is_going_to_state4(self, update):
        text = update.message.text
        if(text == '嘉義'):
            return text.lower() == ('嘉義')
        if (text == '4'):
            return text.lower() == ('4')

    def is_going_to_state5(self, update):
        text = update.message.text
        if(text == '台南'):
            return text.lower() == ('台南')
        if (text == '5'):
            return text.lower() == ('5')

    def is_going_to_state6(self, update):
        text = update.message.text
        if(text == '高雄'):
            return text.lower() == ('高雄')
        if (text == '6'):
            return text.lower() == ('6')

    #顯示台中戲院名稱
    def on_enter_state1(self, update):
        update.message.text="-1"
        res = requests.get("http://www.atmovies.com.tw/showtime/a02/")
        soup = BeautifulSoup(res.text, "html.parser")
        theater = soup.find(id="theaterList")
        theaterp = theater.find_all('a')
        global movielist
        global datalist       
        movielist=[""]
        datalist=[""]

        i=0
        global count
        count=1
        numTheater=['']
        for item in theaterp:
            x = theaterp[i].text
            try:
                data = item['href']
            except:
                print("")
            x=x.strip()
            i=i+1
            if i%3 == 1:
                movielist.append(str(count) +"."+ x + "\n")
                datalist.append(ROOT+data+"\n")
                numTheater.append(str(count))
                count = count+1

        Theater=['']       
        for i in range(1,len(numTheater),8):
            b = numTheater[i:i+8]
            Theater.append(b)

        a = "".join(str(s) for s in movielist)
        custom_keyboard = [Theater[0],Theater[1],Theater[2],Theater[3],
                            Theater[4],Theater[5],Theater[6],['返回']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("TAIPEI 台北\n"+a,reply_markup=reply_markup)
        self.advance(update)



    def on_enter_state2(self, update):
        update.message.text="-1"
        res = requests.get("http://www.atmovies.com.tw/showtime/a04/")
        soup = BeautifulSoup(res.text, "html.parser")
        theater = soup.find(id="theaterList")
        theaterp = theater.find_all('a')
        global movielist
        global datalist       
        movielist=[""]
        datalist=[""]

        i=0
        global count
        count=1
        numTheater=['']
        for item in theaterp:
            x = theaterp[i].text
            try:
                data = item['href']
            except:
                print("")
            x=x.strip()
            i=i+1
            if i%3 == 1:
                movielist.append(str(count) +" ."+ x + "\n")
                datalist.append(ROOT+data+"\n")
                numTheater.append(str(count))
                count = count+1

        Theater=['']       
        for i in range(1,len(numTheater),7):
            b = numTheater[i:i+7]
            Theater.append(b)

        a = "".join(str(s) for s in movielist)
        custom_keyboard = [Theater[0],Theater[1],Theater[2],['返回']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("TAICHUNG 台中\n"+a,reply_markup=reply_markup)
        self.advance(update)


    def on_enter_state3(self, update):
        update.message.text="-1"
        res = requests.get("http://www.atmovies.com.tw/showtime/a47/")
        soup = BeautifulSoup(res.text, "html.parser")
        theater = soup.find(id="theaterList")
        theaterp = theater.find_all('a')
        global movielist
        global datalist       
        movielist=[""]
        datalist=[""]

        i=0
        global count
        count=1
        numTheater=['']
        for item in theaterp:
            x = theaterp[i].text
            try:
                data = item['href']
            except:
                print("")
            x=x.strip()

            i=i+1
            if i%3 == 1:
                movielist.append(str(count) +"."+ x + "\n")
                datalist.append(ROOT+data+"\n")
                numTheater.append(str(count))
                count = count+1
        
        a = "".join(str(s) for s in movielist)
        custom_keyboard = [numTheater,['返回']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("CHANGHUA 彰化\n"+a,reply_markup=reply_markup)
        update.message.text="-1"
        self.advance(update)

    def on_enter_state4(self, update):
        update.message.text="-1"
        res = requests.get("http://www.atmovies.com.tw/showtime/a05/")
        soup = BeautifulSoup(res.text, "html.parser")
        theater = soup.find(id="theaterList")
        theaterp = theater.find_all('a')
        global movielist
        global datalist       
        movielist=[""]
        datalist=[""]

        i=0
        global count
        count=1
        numTheater=['']
        for item in theaterp:
            x = theaterp[i].text
            try:
                data = item['href']
            except:
                print("")
            x=x.strip()
            i=i+1
            if i%3 == 1:
                movielist.append(str(count) +"."+ x + "\n")
                datalist.append(ROOT+data+"\n")
                numTheater.append(str(count))
                count = count+1
        a = "".join(str(s) for s in movielist)
        custom_keyboard = [numTheater,['返回']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("CHAIYI 嘉義\n"+a,reply_markup=reply_markup)
        update.message.text="-1"
        self.advance(update)

    def on_enter_state5(self, update):
        update.message.text="-1"
        res = requests.get("http://www.atmovies.com.tw/showtime/a06/")
        soup = BeautifulSoup(res.text, "html.parser")
        theater = soup.find(id="theaterList")
        theaterp = theater.find_all('a')
        global movielist
        global datalist       
        movielist=[""]
        datalist=[""]

        i=0
        global count
        count=1
        numTheater=['']
        for item in theaterp:
            x = theaterp[i].text
            try:
                data = item['href']
            except:
                print("")
            x=x.strip()
            i=i+1
            if i%3 == 1:
                movielist.append(str(count) +"."+ x + "\n")
                datalist.append(ROOT+data+"\n")
                numTheater.append(str(count))
                count = count+1
        a = "".join(str(s) for s in movielist)
        custom_keyboard = [numTheater,['返回']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("TAINAN 台南\n"+a,reply_markup=reply_markup)
        update.message.text="-1"
        self.advance(update)

    def on_enter_state6(self, update):
        update.message.text="-1"
        res = requests.get("http://www.atmovies.com.tw/showtime/a07/")
        soup = BeautifulSoup(res.text, "html.parser")
        theater = soup.find(id="theaterList")
        theaterp = theater.find_all('a')
        global movielist
        global datalist       
        movielist=[""]
        datalist=[""]

        i=0
        global count
        count=1
        numTheater=['']
        for item in theaterp:
            x = theaterp[i].text
            try:
                data = item['href']
            except:
                print("")
            x=x.strip()
            i=i+1
            if i%3 == 1:
                movielist.append(str(count) +"."+ x + "\n")
                datalist.append(ROOT+data+"\n")
                numTheater.append(str(count))
                count = count+1

        Theater=['']       
        for i in range(1,len(numTheater),5):
            b = numTheater[i:i+5]
            Theater.append(b)

        a = "".join(str(s) for s in movielist)
        custom_keyboard = [Theater[0],Theater[1],Theater[2],Theater[3],['返回']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("KAOHSIUNG 高雄\n"+a,reply_markup=reply_markup)
        self.advance(update)


    def is_going_to_backgarbage(self, update):
        text = update.message.text
        if(text == '返回'):
            return text.lower() == ('返回')
        if (text == 'back'):
            return text.lower() == ('back')

    def on_enter_backgarbage(self, update):
        update.message.text="-1"
        self.go_garbage(update)


    def is_going_to_taichung(self, update):
        global j
        global movielist
        global datalist 
        global movieUrl 
        global choose 
        text = update.message.text
        j=text
        choose=text
        try:
            movieUrl = datalist[int(j)]
            if int(text)>=0:
                return text.lower() == (j)
        except:
            update.message.reply_text('乖啦認真輸入')
            print('taichung')


    #顯示電影名稱
    def on_enter_taichung(self, update):
        update.message.text="-1"
        global j
        global movieelist
        global datalist 
        global movieUrl
        global storylist
        global check
        global choose
        check=0

        movieUrl = datalist[int(choose)].strip()
        res = requests.get(movieUrl)
        soup = BeautifulSoup(res.text, "html.parser")

        movie = soup.find(id="theaterShowtimeBlock")
        moviep = movie.find_all('li', 'filmTitle')
        moviever = soup.find_all(id="theaterShowtimeTable")
        movieelist=[""]
        timelist=[""]
        storylist=[""]

        i=0
        count = 1
        for item in moviep:
            try:
                ver=moviever[i].find('li','filmVersion').text
                #print(ver)
            except:
                ver=""
            story = item.find('a')['href']
            storylist.append(ROOT+story+"\n")
            name = soup.select('.filmTitle')[i].text.strip()
            i=i+1
            movieelist.append(str(count) +" ."+name+" "+ver+"\n")
            count=count+1
        a="".join(str(s) for s in movieelist)
        reply_markup = telegram.ReplyKeyboardHide()
        update.message.reply_text(movielist[int(choose)]+"\n"+datalist[int(choose)]+"\n"+a,
                                    reply_markup=reply_markup)
        self.advance(update)

    #判斷要看時間還是簡介...
    def is_going_to_storyortime(self, update):
        global j   
        global movieelist
        global test
        text = update.message.text
        j=text
        choose = j
        try:
            test = movieelist[int(j)]
            if int(text)>=0:
                return text.lower() == (j)
        except:
            print('storyortime')
            update.message.reply_text('乖啦認真輸入')
        

    def on_enter_storyortime(self, update):
        update.message.text="-1"
        global j 
        global movieelist
        global storylist
        global storyUrl
        global check

        if check==0:
            update.message.reply_text(movieelist[int(j)] + storylist[int(j)])

        custom_keyboard = [['時間','簡介','卡司','預告'],['返回','結束']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text("查看電影資訊",reply_markup=reply_markup)

        storyUrl = storylist[int(j)].strip()
        self.advance(update)


    def is_going_to_tcmovietime(self, update):
        text = update.message.text
        return text.lower() == ('時間')

    #顯示電影時間
    def on_enter_tcmovietime(self, update):
        update.message.text="-1"
        global j
        global movielist
        global datalist 
        global movieUrl
        global check
        check=1

        res = requests.get(movieUrl)
        soup = BeautifulSoup(res.text, "html.parser")

        movie = soup.find(id="theaterShowtimeBlock")

        moviep = movie.find_all(id="theaterShowtimeTable")
        movieelist=[""]
        timelist=[""]
        total = [""]
        i=0
        count = 1
        for item in moviep:
            movieelist=[""]
            timelist=[""]
            name = soup.select('.filmTitle')[i].text.strip()
            i=i+1
            movieelist.append(str(count) +"."+name+"\n")
            count=count+1
            #print(name)

            cut = item.find_all('li')
            
            pat = re.compile(r'\d\d\：\d\d')
            tt=re.findall(pat,str(cut[1]))
            for t in tt:
                timelist.append(t+"\n")
            a="".join(str(s) for s in timelist)
            total.append(a)
            
        update.message.text=j
        update.message.reply_text("\n"+total[int(j)])
        self.go_movie_choose(update)

    #顯示電影簡介及網頁
    def is_going_to_tcmoviestory(self, update):
        text = update.message.text
        return text.lower() == ('簡介')

    def on_enter_tcmoviestory(self, update):
        update.message.text="-1"
        global storyUrl
        global j
        global check
        check=1
        update.message.reply_text("看故事囉")

        res = requests.get(storyUrl)
        soup = BeautifulSoup(res.text, "html.parser")

        catch = soup.find(id='filmTagBlock')
        img = catch.find('img')['src']
        #print(img)

        catch = soup.find('div','content content-left')
        story = soup.find('br').text.strip()
        #print(story)
       
        update.message.reply_photo(img)
        update.message.reply_text(story)
        update.message.text=j
        self.go_movie_choose(update)

    #顯示演員卡司
    def is_going_to_cast(self, update):
        text = update.message.text
        return text.lower() == ('卡司')

    def on_enter_cast(self, update):
        update.message.text="-1"
        global storyUrl
        global j
        global check
        check=1
        #update.message.reply_text("看帥哥囉")
        #update.message.reply_text(storyUrl)
        
        castUrl = storyUrl.split('/')[5]
        castUrl = CAST+castUrl+"/"
        #update.message.reply_text(castUrl)
        
        res = requests.get(castUrl)
        soup = BeautifulSoup(res.text, "html.parser")
        castlist=[""]
        people = soup.find('div','content content-left')
        allpeople = people.find_all('li')
        for item in allpeople:
            castlist.append(item.text+"\n")
        a="".join(str(s) for s in castlist)
        update.message.reply_text(a)
        update.message.text=j
        self.go_movie_choose(update)

    #顯示預告片
    def is_going_to_video(self, update):
        text = update.message.text
        return text.lower() == ('預告')

    def on_enter_video(self, update):
        update.message.text="-1"
        global storyUrl
        global j
        global check
        check=1
        res = requests.get(storyUrl)
        soup = BeautifulSoup(res.text, "html.parser")

        try:
            video = soup.find('div','video_view')
            videoUrl = video.find('iframe')['src']
            #print(videoUrl)
            update.message.reply_text(videoUrl)
            #update.message.reply_video(videoUrl)
        except:
            update.message.reply_text("對不起，這部電影未找到預告片喔")
        update.message.text=j
        self.go_movie_choose(update)

    #結束
    def is_going_to_ok(self, update):
        text = update.message.text
        return text.lower() == ('結束')

    def on_enter_ok(self, update):
        reply_markup = telegram.ReplyKeyboardHide()
        update.message.reply_text("回來～～",reply_markup=reply_markup)
        self.go_back(update)

    def is_going_to_backMovie(self, update):
        text = update.message.text
        return text.lower() == ('返回')

    def on_enter_backMovie(self, update):
        update.message.text="-1"
        update.message.reply_text("back to mivie")
        self.back_to_movie(update)


    def on_exit_taichung(self, update):
        print('Leaving taichung')

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_exit_state2(self, update):
        print('Leaving state2')
    def on_exit_state3(self, update):
        print('Leaving state3')
