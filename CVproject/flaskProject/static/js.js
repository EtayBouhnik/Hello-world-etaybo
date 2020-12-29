
  // button with function that change attribute.

function rep() { 
  document.body.innerHTML  = document.body.innerHTML.replace("The greatest pleasure in life is doing what people say you can not.", "When you are right - you learn what you know. When you make a mistake - you learn new things."); 
} 
function rep1() { 
  document.body.innerHTML  = document.body.innerHTML.replace( "When you are right - you learn what you know. When you make a mistake - you learn new things.","The greatest pleasure in life is doing what people say you can not."); 
} 
function changeImage() {
  var image = document.getElementById('myImage');
  if (image.src.match("/pp.jpg")) {
      image.src = "/face-p.jpg";
  }
  else {
      image.src = "/pp.jpg";
  }
}
function ValidateEmail(inputText)
{
var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
if(inputText.value.match(mailformat))
{
alert("Valid email address!");
document.form1.text1.focus();
return true;
}
else
{
alert("You have entered an invalid email address!");
document.form1.text1.focus();
return false;
}
}