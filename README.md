# E-driving Surveillance System
 <h3>教習所予約監視プログラム</h3>
 Surveillance program for driving school
 

教習所の予約があまりにもとれないために予約の空を通知するために作ったものです。<br>
基本的にはこのままのシステムでは私の通っている教習所でしか使えません<br>
<strong>（個人の特定のためアドレス等情報をすべて隠しているため、どちらにしろ使えないですが、）</strong><br>
参考程度と考えてください。<br>

プログラム自体に繰り返し連続で実行・通知する能力はありません。<br>
Windowsタスクスケジューラと一緒に利用することで最短1分おきにサイトにアクセス・確認を行います。
<dl>
<dt>プログラムで実現されていること</dt>
<dd>サイトへのアクセス・スクレイピング</dd>
<dd>解析後、各時限毎の状況を表すClassを抽出</dd>
<dd>空時限に該当するclassがあった場合のみLINE&Gmailで通知</dd>

 <dt>タスクスケジューラにて実現すること</dt>
<dd>定期時間ごとの繰り返し実行</dd>
</dl>
空が出たときのみに通知をするシステムですがLINE Notifyの通知上限が1000回/時間 なので考慮してアレンジしてください<br>
<br>
また、教習所のシステムによっては負荷をかけてしまう場合があります。<br>
類似システムを作成した場合は、各学校のシステムの様子を見ながら迷惑をかけないよう使用してください。
<br>
2021/5/21
