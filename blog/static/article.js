const link = 'http://127.0.0.1:8000/'
var news = document.getElementById('article-id');
var news_id = news.innerHTML;
request = {'id': news_id}
$.ajax({
    type: 'GET',
    url : `${link}comment/`,
    data: request,
    success: function(response){
        for(var i=0; i < response.comments.length; i++) {
            $(".container").append(
                `
                    <p> ${response.comments[i].text}</p>
                `
            )
        }
    },
    error: function(error) {
        console.log(error)
    }
})