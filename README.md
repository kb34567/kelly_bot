# kelly_bot

## STATE圖片
![image](https://github.com/kb34567/kelly_bot/blob/master/show-fsm.png)

## 用法
1.  init:一開始隨便打字跟它聊天，
    它就會請你輸入，或是按按鈕選擇你要的地區的戲院

2.  state1,2,3,4,5,6:之後進入那地區，就可以選擇你要的戲院，
    選好後進入該戲院
    若你亂輸入它就會說"乖啦～認真輸入"

3.  taichung:可以選擇那部戲院現在有上的電影，
    這裡要自己打數字喔～
    若你亂輸入它就會說"乖啦～認真輸入"

4.  storyortime:進去那部電影之後，
    可以選擇要看時刻表(tcmovietime)，電影介紹(tcmoviestory)，卡司(cast)，預告片(video)，
    顯示電影介紹時還會給你看電影的海報，

    選擇完後會自動回去上一個state，
    所以可以繼續選你要看時刻表，電影介紹，卡司，預告片，
    也可以返回重新選電影，
    或是結束，它就會跟你說"回來～～"
