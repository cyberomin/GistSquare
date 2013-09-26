import sendgrid


s = sendgrid.Sendgrid('cyberomin', 'Ropacel1234!', secure=True)



body = """
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns="http://www.w3.org/1999/html">
<head>
<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />

<!-- Facebook sharing information tags -->
<meta property='og:title' content='*|MC:SUBJECT|*' />

<title>*|MC:SUBJECT|*</title>
<style type='text/css'>
    /* Client-specific Styles */
#outlook a{padding:0;} /* Force Outlook to provide a 'view in browser' button. */
body{width:100% !important;} .ReadMsgBody{width:100%;} .ExternalClass{width:100%;} /* Force Hotmail to display emails at full width */
body{-webkit-text-size-adjust:none;} /* Prevent Webkit platforms from changing default text sizes. */

    /* Reset Styles */
body{margin:0; padding:0;}
img{border:0; height:auto; line-height:100%; outline:none; text-decoration:none;}
table td{border-collapse:collapse;}
#backgroundTable{height:100% !important; margin:0; padding:0; width:100% !important;}

    /* Template Styles */

    /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: COMMON PAGE ELEMENTS /\/\/\/\/\/\/\/\/\/\ */

    /**
    * @tab Page
    * @section background color
    * @tip Set the background color for your email. You may want to choose one that matches your company's branding.
    * @theme page
    */
body, #backgroundTable{
    /*@editable*/ background-color:#FAFAFA;
}

    /**
    * @tab Page
    * @section email border
    * @tip Set the border for your email.
    */
#templateContainer{
    /*@editable*/ /*border: 1px solid #DDDDDD;*/
    /*background:url(http://cyberomin.com/KongaNewsletterElement/newsletterShadow.jpg) repeat-y #FFF;
    width:700px;*/
    /*-moz-box-shadow: 0 0 8px #999999;
     -webkit-box-shadow: 0 0 8px #999999;
    box-shadow: 0 0 8px #999999;*/
}

    /**
    * @tab Page
    * @section heading 1
    * @tip Set the styling for all first-level headings in your emails. These should be the largest of your headings.
    * @style heading 1
    */
h1, .h1{
    /*@editable*/ color:#202020;
    display:block;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:34px;
    /*@editable*/ font-weight:bold;
    /*@editable*/ line-height:100%;
    margin-top:0;
    margin-right:0;
    margin-bottom:10px;
    margin-left:0;
    /*@editable*/ text-align:left;
}

    /**
    * @tab Page
    * @section heading 2
    * @tip Set the styling for all second-level headings in your emails.
    * @style heading 2
    */
h2, .h2{
    /*@editable*/ color:#202020;
    display:block;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:30px;
    /*@editable*/ font-weight:bold;
    /*@editable*/ line-height:100%;
    margin-top:0;
    margin-right:0;
    margin-bottom:10px;
    margin-left:0;
    /*@editable*/ text-align:left;
}

    /**
    * @tab Page
    * @section heading 3
    * @tip Set the styling for all third-level headings in your emails.
    * @style heading 3
    */
h3, .h3{
    /*@editable*/ color:#202020;
    display:block;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:26px;
    /*@editable*/ font-weight:bold;
    /*@editable*/ line-height:100%;
    margin-top:0;
    margin-right:0;
    margin-bottom:10px;
    margin-left:0;
    /*@editable*/ text-align:left;
}

    /**
    * @tab Page
    * @section heading 4
    * @tip Set the styling for all fourth-level headings in your emails. These should be the smallest of your headings.
    * @style heading 4
    */
h4, .h4{
    /*@editable*/ color:#202020;
    display:block;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:22px;
    /*@editable*/ font-weight:bold;
    /*@editable*/ line-height:100%;
    margin-top:0;
    margin-right:0;
    margin-bottom:10px;
    margin-left:0;
    /*@editable*/ text-align:left;
}

    /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: HEADER /\/\/\/\/\/\/\/\/\/\ */

    /**
    * @tab Header
    * @section header style
    * @tip Set the background color and border for your email's header area.
    * @theme header
    */
#templateHeader{
    /*@editable*/ background-color:#FFFFFF;
    /*@editable*/ border-bottom:0;
}

    /**
    * @tab Header
    * @section header text
    * @tip Set the styling for your email's header text. Choose a size and color that is easy to read.
    */
.headerContent{
    /*@editable*/ color:#202020;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:34px;
    /*@editable*/ font-weight:bold;
    /*@editable*/ line-height:100%;
    /*@editable*/ padding:0;
    /*@editable*/ text-align:right;
    /*@editable*/ vertical-align: top;
}

    /**
    * @tab Header
    * @section header link
    * @tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
    */
.headerContent a:link, .headerContent a:visited, /* Yahoo! Mail Override */ .headerContent a .yshortcuts /* Yahoo! Mail Override */{
    /*@editable*/ color:#336699;
    /*@editable*/ font-weight:normal;
    /*@editable*/ text-decoration:underline;
}

#headerImage{
    height:auto;
    max-width:600px !important;
}

    /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: MAIN BODY /\/\/\/\/\/\/\/\/\/\ */

    /**
    * @tab Body
    * @section body style
    * @tip Set the background color for your email's body area.
    */
#templateContainer, .bodyContent{
    /*@editable*/ background-color:#FFFFFF;
}

    /**
    * @tab Body
    * @section body text
    * @tip Set the styling for your email's main content text. Choose a size and color that is easy to read.
    * @theme main
    */
.bodyContent div{
    /*@editable*/ color:#505050;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:14px;
    /*@editable*/ line-height:150%;
    /*@editable*/ text-align:left;
}

    /**
    * @tab Body
    * @section body link
    * @tip Set the styling for your email's main content links. Choose a color that helps them stand out from your text.
    */
.bodyContent div a:link, .bodyContent div a:visited, /* Yahoo! Mail Override */ .bodyContent div a .yshortcuts /* Yahoo! Mail Override */{
    /*@editable*/ color:#336699;
    /*@editable*/ font-weight:normal;
    /*@editable*/ text-decoration:underline;
}

    /**
    * @tab Body
    * @section button style
    * @tip Set the styling for your email's button. Choose a style that draws attention.
    */
.templateButton{
    text-align:center;
}

    /**
    * @tab Body
    * @section button style
    * @tip Set the styling for your email's button. Choose a style that draws attention.
    */
.templateButton, .templateButton a:link, .templateButton a:visited, /* Yahoo! Mail Override */ .templateButton a .yshortcuts /* Yahoo! Mail Override */{
    /*@editable*/ color:#FFFFFF;
    /*@editable*/ font-family: Verdana, Geneva, sans-serif;

    /*@editable*/ letter-spacing:-.5px;
    /*@editable*/
    text-align:center;
    text-decoration:none;
}

.bodyContent img{
    display:inline;
    height:auto;
}

    /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: FOOTER /\/\/\/\/\/\/\/\/\/\ */

    /**
    * @tab Footer
    * @section footer style
    * @tip Set the background color and top border for your email's footer area.
    * @theme footer
    */
#templateFooter{
    /*@editable*/ background-color:#FFFFFF;
    /*@editable*/ border-top:0;
}

    /**
    * @tab Footer
    * @section footer text
    * @tip Set the styling for your email's footer text. Choose a size and color that is easy to read.
    * @theme footer
    */
.footerContent div{
    /*@editable*/ color:#707070;
    /*@editable*/ font-family:Arial;
    /*@editable*/ font-size:12px;
    /*@editable*/ line-height:125%;
    /*@editable*/ text-align:center;
}

    /**
    * @tab Footer
    * @section footer link
    * @tip Set the styling for your email's footer links. Choose a color that helps them stand out from your text.
    */
.footerContent div a:link, .footerContent div a:visited, /* Yahoo! Mail Override */ .footerContent div a .yshortcuts /* Yahoo! Mail Override */{
    /*@editable*/ color:#336699;
    /*@editable*/ font-weight:normal;
    /*@editable*/ text-decoration:underline;
}

.footerContent img{
    display:inline;
}

    /**
    * @tab Footer
    * @section utility bar style
    * @tip Set the background color and border for your email's footer utility bar.
    * @theme footer
    */
#utility{
    /*@editable*/ background-color:#FFFFFF;
    /*@editable*/ border:0;
}

    /**
    * @tab Footer
    * @section utility bar style
    * @tip Set the background color and border for your email's footer utility bar.
    */
#utility div{
    /*@editable*/ /*text-align:center;*/
}

#monkeyRewards img{
    max-width:190px;
}
#utility a
{
    color:#FFF;
    text-decoration:none;
}
#utility a:hover
{
    text-decoration:underline;
}
</style>
</head>
<body leftmargin='0' marginwidth='0' topmargin='0' marginheight='0' offset='0' style="background-color: #DDDDDD">
<div style="background-color:#DDDDDD; border-right:solid 1px #CCCCCC">
<table border='0' cellpadding='0' cellspacing='0' height='100%' width='100%' id='backgroundTable'
       style='border-right:solid 1px #CCCCCC'>

<tr>
<td align='center' valign='top' style='padding-top:20px;'>

<table border='0' cellpadding='0' cellspacing='0' width='600' style="background-color: #FFFFFF">

<tr>
    <td align='center' valign="middle">

        <!-- // Begin Template Header \\ -->
        <table border='0' cellpadding='0' cellspacing='0' width='600' id='templateHeader' style='padding-top:20px'>
            <tr>
                <td align='left'>

                    <!-- // Begin Module: Standard Header Image \\ -->

                    <a href="http://gistsquare.com">
                        <img src='http://gistsquare.com/static/assets/images/logo.png' style="margin-left:5px"/>
                    </a>
                    <!-- // End Module: Standard Header Image \\ -->

                </td>

                <td align='center'>

                    <!-- // Begin Module: Standard Header Image \\ -->


                    <!-- // End Module: Standard Header Image \\ -->

                </td>
                <td align='right'>



                    <!-- // End Module: Standard Header Image \\ -->

                </td>
            </tr>
        </table>



        <div style='padding:5px;' id='utility'>
            <table style='margin-top:5px; width:99%;border-top:solid 1px #CCCCCC;border-bottom: solid 1px #CCCCCC;' cellpadding="0" cellspacing="0">
                <tr style="
                        font-family:Verdana, Geneva, sans-serif;
                        font-size:13.2px; font-weight:500; text-align: left">


                    <td>
                        <a href="http://gistsquare.com" style=" color:#325D88; text-decoration:none; line-height:40px;">
                            Conversation that matters, when it matters!
                        </a>
                    </td>



                </tr>
            </table>
        </div>

        <!-- // End Template Header \\ -->
    </td>
</tr>
<tr>
    <td align='center' valign='top' style="font-family:Verdana, Geneva, sans-serif; font-size:12px">
        <!-- // Begin Template Body \\ -->
        <table border='0' cellpadding='0' cellspacing='0' width='600' id='templateBody'>
            <tr>
                <td valign='top'>

                    <!-- // Begin Module: Standard Content \\ -->
                    <table border='0' cellpadding='5' cellspacing='0' width='100%' style='margin-top:1px;'>

                        <tr align="center">

                            <td align="center">
                                 <span style="font-size: 18px;padding-left: 25px; margin-bottom: 5px; display:block; float:left">Hi there, here's today's top stories</span>
                                 <div style="clear:both"></div>
                                <div style="text-align: left; font-size: 14px; font-family:Verdana, Geneva, sans-serif; color: #333333; width: 550px">



                                    <div style="border: solid 1px #CDCDCD; padding: 5px; color: #999; line-height:1.4; margin-bottom: 15px">
                                        <span style="display:block; color: #333333; font-weight: 600">Google News</span>
                                        <img src="http://sabotagetimes.com/wp-content/uploads/Inter-coach-Jose-Mourinho-001.jpg" alt="" style="float: right; width:90px; height:auto "/>
                                        BBC SportChampions League: Jose Mourinho confident Chelsea will progressSkySportsChelsea boss Jose Mourinho remains confident that his side will qualify for the knockout stages of the Champions League, despite their loss at home to Basel. The Swiss side came from a goal behind to win 2-1 on Wednesday<br>
                                        <a href="http://gistsquare.com/story/149/" style="color:#3a87ad;text-decoration:none">[Read More]</a>
                                        <span style="color: #CCC; display: block">1 hour ago</span>
                                    </div>

                                    <div style="border: solid 1px #CDCDCD; padding: 5px; color: #999; line-height:1.4; margin-bottom:15px">
                                        <span style="display:block; color: #333333; font-weight: 600">Google News</span>
                                        <img src="http://eplwire.com/wp-content/uploads/2013/05/wenger.jpg" alt="" style="float: right; width:90px; height:auto "/>
                                        Telegraph.co.ukArsene Wenger thrilled to take three points from 'tricky' Champions League ...Telegraph.co.ukTheo Walcott and Aaron Ramsey scored the all-important goals at the intimidating - if half finished - Stade Velodrome, where the Gunners rode their luck in securing a 2-1 win. While the performance was not perfect, Wenger could not ... <br>
                                        <a href="http://gistsquare.com/story/152/" style="color:#3a87ad;text-decoration:none">[Read More]</a>
                                        <span style="color: #CCC; display: block">1 hour ago</span>
                                    </div>

                                    <div style="border: solid 1px #CDCDCD; padding: 5px; color: #999; line-height:1.4">
                                        <span style="display:block; color: #333333; font-weight: 600">Super Sports</span>
                                        <img src="http://cdn.dstv.com/supersport.img/website/images/update_Logo.png" alt="" style="float: right; width:90px; height:auto "/>
                                        SuperSport (blog)Chukwu predicts Eagles' CHAN glorySuperSport (blog)Former Nigerian manager, Christian Chukwu is upbeat Nigeria will qualify from the tough group at the 2014 African Nations Championship (Chan) in South Africa. The Chan draw on Wednesday at the Caf headquarters in Cairo, Egypt pitched Nigeria,...Bafana face tough African Nations Championship opponentsBDliveTough ... <br>
                                        <a href="http://gistsquare.com/story/148/" style="color:#3a87ad;text-decoration:none">[Read More]</a>
                                        <span style="color: #CCC; display: block">1 hour ago</span>
                                    </div><br>
                                  Read more news on <a href="http://gistsquare.com" style="color:#3a87ad;text-decoration:none">Gistquare.</a>

                                </div>
                            </td>
                        </tr>



                        <tr>
                            <td align="center">
                                <br>
                                <!--<span style="display: block; font-size: 25px">GET SOCIAL</span>!-->
                                <a href="http://facebook.com/gistsquare"><img src='https://s3.amazonaws.com/KongaNewsletters/elements/facebook_new.png'/></a>
                                <a href="http://twitter.com/gistsquare"><img src='https://s3.amazonaws.com/KongaNewsletters/elements/twitter_new.png'/></a>

                            </td>
                        </tr>

                    </table>
                </td>
            </tr>

        </table>
        <!-- // End Module: Standard Content \\ -->

    </td>
</tr>




</table>
<!-- // End Template Body \\ -->
</td>
</tr>
<tr>
    <td align='center' valign='top'>
        <!-- // Begin Template Footer \\ -->
        <table border='0' cellpadding='10' cellspacing='0' width='600' id='templateFooter' >
            <tr>
                <td valign='top' class='footerContent'>

                    <!-- // Begin Module: Transactional Footer \\ -->
                    <table border='0' cellpadding='10' cellspacing='0' width='100%'>
                        <tr>
                            <td valign='top' class='templateButton' align='center'>

                                <div mc:edit='std_footer'>







                                </div>
                            </td>
                        </tr>

                    </table>
                    <!-- // End Module: Transactional Footer \\ -->

                </td>
            </tr>
        </table>
        <table border='0' cellpadding='10' cellspacing='0' width='600' id='templateFooter'
               style='border-top:solid 1px #CCCCCC; font-family:verdana'>
            <tr>
                <td valign='top' class='footerContent'>

                    <!-- // Begin Module: Transactional Footer \\ -->
                    <table border='0' cellpadding='10' cellspacing='0' width='100%' >


                        <tr>
                            <td valign='middle' id='utility' align='center'>
                                <div mc:edit='std_utility' style='color:#666666; font-size:10px;'>
                                    PLEASE DO NOT REPLY TO THIS MESSAGE<br/>
                                    This is a system generated <span style='color:#EE8C1D; display:inline-block'>gistsquare.com</span> email. Replies will not be
                                    read or forwarded for handling
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td valign='middle' id='utility' align='center'>
                                <div mc:edit='std_utility' style='color:#666666; font-size:10px;'>

                                    <a href="[unsubscribe]" style='color:#666666'>Unsubscribe</a><br/>
                                    Copyright 2013 Gistsquare. All rights reserved
                                </div>
                            </td>
                        </tr>
                    </table>
                    <!-- // End Module: Transactional Footer \\ -->


                </td>
            </tr>

        </table>
        <!-- // End Template Footer \\ -->
    </td>
</tr>
</table>
<br />
</td>
</tr>
</table>
</div>
<script type='text/javascript'>
   (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43714038-1', 'gistsquare.com');
  ga('send', 'pageview');

</script>
</body>
</html>
"""




sender = ("noreply@gistsquare.com","Gistsquare")
message = sendgrid.Message(sender, "Daily Digest", "",body)
message.add_to("celestineomin@gmail.com", "Celestine Omin")
message.add_bcc(["celestine@konga.com","cyberomin@yahoo.com"])

s.web.send(message)