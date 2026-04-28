let nav;
document.addEventListener("scroll", (e) => {
  if (!nav) nav = document.getElementsByTagName("nav")[0];
  nav.toggleAttribute("data-active", window.scrollY > 50);
});
