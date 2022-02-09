const container = document.getElementsByClassName("mobile_container").item(0);
console.log(container);
container.addEventListener("click", () => {
  const list = document.getElementsByClassName("hamburger_menu").item(0);
  console.log(list);
  console.log(list.classList.contains("hidden"));
  list.classList.contains("hidden")
    ? list.classList.remove("hidden")
    : list.classList.add("hidden");
});
