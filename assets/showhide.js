function addListeners() {
  let lLM = document.querySelector(".lLM")
  let sLM = document.querySelector(".learnMore")

  lLM.addEventListener("click", function(){
      sLM.classList.toggle("hide");
  });

}

document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {addListeners()}, 1000)
})