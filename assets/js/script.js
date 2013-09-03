$(document).ready(function()
{

    var searchBox = $("#search");
    var resultPanel = $("#search_results");

    searchBox.focus(function()
    {
        $(this).css("outline","none")

    })

    var csrf_token = $("input[name=csrfmiddlewaretoken]").val();

    //console.log($("input[name=csrfmiddlewaretoken]").val());
    searchBox.keyup(function()
    {
        if (searchBox.val().length >= 3)
        {
            resultPanel.show();
            if ($.trim(searchBox.val()).length > 0)
            {
                $.ajax({
                    type: "POST",
                    url : "/search/",
                    data: {
                        'search_text' : searchBox.val(),
                        'csrfmiddlewaretoken':csrf_token
                    },
                    success:function(data)
                    {
                        var style = {
                            width: '99.8%',
                            border: 'solid 1px #CCCCCC',
                            height: 'auto',
                            borderTop :'none',
                            boxShadow:'0 1px 2px rgba(200,200,200,0.5)',
                            backgroundColor: '#FFFFFF'
                        }
                        searchBox.css("border-bottom","none");
                        resultPanel.css(style);
                        resultPanel.html(data);
                    },
                    dataType:"html"
                })
            }
            else
            {
                searchBox.css("border-bottom","solid 1px #CCCCCC");
                var style = {
                    border:'none'
                }
                resultPanel.css(style).empty();
            }
        }
        else
        {
            searchBox.css("border-bottom","solid 1px #CCCCCC");
            resultPanel.hide();
        }
    })

    //Subscribe
    $("#email_form").submit(function()
    {
        var email = $("#email");
        var resultPanel =  $(".sub_results");
        if (email.val() == "")
        {
             resultPanel.html("<span class='sub_error'>Enter an email address</span>");
            return false;
        }
        else
        {
            $.ajax({
                type: "POST",
                url : "/subscription/",
                data: {
                    'email' : email.val(),
                    'csrfmiddlewaretoken':csrf_token
                },
                success:function(data)
                {
                    email.val("");
                    $(".sub_results").empty()
                    if (data == "Email already exits" || data == "Invalid Email")
                    {
                        resultPanel.html("<span class='sub_error'>"+data+"</span>")
                    }
                    else
                    {
                        resultPanel.html("<span class='sub_success'>"+data+"</span>")
                    }
                },
                dataType:"html"
            })
        }

        return false
    })
})