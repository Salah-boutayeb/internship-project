console.log('heey');
$(document).ready(function(){
    $('.collapsible').collapsible();
  });
$(document).ready(function(){
$('.tap-target').tapTarget();
});

/* $.ajax({
type: 'GET',
url:`/stages/`,
success: (response)=>{
    console.log(response);
},
error: (error)=>{
    console.error(error);
},
}) */
$(document).ready(function(){
    $('.modal').modal();
  })