$(document).on('submit','#post-ingredients',function(e)
{
console.log('hello');
e.preventDefault();
$.ajax({
type:'POST',
url:'/',
data:{
food:$("#ingredients").val()
},
success: function(response) {
$("#main-page").html(response);
},
error: function(xhr) {
//Do Something to handle error
}
})
});