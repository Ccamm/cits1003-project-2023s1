<?php
if(!isset($_COOKIE["user"])){ 
    setcookie("user", "Guest");
    $_COOKIE["user"] = "Guest";
}
?>

<html>
    <head>
        <title>🐧 Skipper's Cookies 🐧</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <style>
        h1 {text-align: center;}
        h3 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
        ul {text-align: center;}
        li {text-align: center;}
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            /* width: 50%; */
            height: 50%;
        }
        body {
            background-color: rgb(0, 255, 234);
        }
        @keyframes spinning {
            from { transform: rotate(0deg) }
            to { transform: rotate(360deg) }
        }
        .spin {
            animation-name: spinning;
            animation-duration: 3s;
            animation-iteration-count: infinite;
            /* linear | ease | ease-in | ease-out | ease-in-out */
            animation-timing-function: linear;
        }
        </style>
        <script src="/js/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <h1>Skipper's Cookies</h1>
        <?php if ($_COOKIE["user"] === "Skipper") { ?>
            <h3>Welcome back Skipper!</h3>
            <img src="/images/cookie.png" class="spin"/>
            <p>Here is your cookie!</p>
            <p><b>UWA{c0000k13s_N0m_n0m_n0M!!one11!}</b></p>
        <?php } else { ?>
            <h3>Hold it there <?php echo $_COOKIE["user"]; ?>!</h3>
            <img src="/images/skipper-popo.png"/>
            <p>Only <b>Skipper</b> can get access to this <b>Cookie</b></p>
        <?php } ?>
    </body>
</html>