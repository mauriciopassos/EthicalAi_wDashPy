function addListeners() {
  let lLM = document.querySelector(".lLM")
  let sLM = document.querySelector(".learnMore")
  let arrow = document.querySelector(".learnarrow")

  lLM.addEventListener("click", function(){
      sLM.classList.toggle("hide");

      
      right = arrow.classList.contains("bi-arrow-right-short");
      if(right){
        arrow.classList.remove("bi-arrow-right-short");
      }
      else{
        arrow.classList.add("bi-arrow-right-short");
      }
      arrow.classList.toggle("bi-arrow-down-short");
  });

}

document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {addListeners()}, 1000)
})