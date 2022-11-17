function home()
{
    $.ajax({
        type:'POST',
        url:'/login',
        data:{},
        success:function(response)
        {
            document.getElementById('main').innerHTML=response;
        }
    });
}
function signup()
{
    $.ajax({
        type:'POST',
        url:'/register',
        data:{},
        success:function(response)
        {
            document.getElementById('main').innerHTML=response;
        }
    });
}
function about()
{
    $.ajax({
        type:'POST',
        url:'/about',
        data:{},
        success:function(response)
        {
            document.getElementById('main').innerHTML=response;
        }
    });
}
window.onload = function() 
{ 
    $.ajax({
        type: 'POST',
        url: '/login',
        data: {},
        success: function (response) 
        {
            document.getElementById("main").innerHTML=response; 
        }
    });
};
$(document).ready(function(){
    let msg=document.getElementById('msg').value;
    if(msg=='error')
    {
        alertify.set('notifier','position','top-center');
        alertify.error('Invalid Username/Password!');
    }
    else if(msg=='success')
    {
        alertify.set('notifier','position','top-center');
        alertify.notify('Redirecting to home page...', 'success', 3, function(){
            window.location.href='/home';
        });
    }
});

