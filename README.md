# feedly-mail

feedlyを使っていて、良記事や知っておいて欲しい記事とかを部門とかチームとかにまとめて配信するのですが、これも手でやってると結構面倒なので、APIを使って毎日自動配信する事にしました。

公式のAPI情報はこちらです。
<a href="http://developer.feedly.com/v3/" target="_blank">http://developer.feedly.com/v3/</a>


## トークン

<a href="https://cloud.feedly.com/v3/auth/dev" target="_blank">https://cloud.feedly.com/v3/auth/dev</a>のリンク先で普段ログインしている方法でログインします。

facebookとGoogleの場合はメールで、Twitterの場合はダイレクトメッセージでURLが届きますのでそれをクリックします。

これでアクセストークンがとれるのでUSER IDと一緒に記録しておきます。
