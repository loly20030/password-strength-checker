function checkPassword() {
  const password = document.getElementById("password").value;
  const strength = document.getElementById("strength");
  const rules = document.getElementById("rules");

  let score = 0;
  rules.innerHTML = "";

  function addRule(condition, text) {
    const li = document.createElement("li");
    li.textContent = text;
    li.style.color = condition ? "lightgreen" : "red";
    rules.appendChild(li);

    if (condition) score++;
  }

  addRule(password.length >= 8, "Au moins 8 caractères");
  addRule(/[A-Z]/.test(password), "Contient une majuscule");
  addRule(/[a-z]/.test(password), "Contient une minuscule");
  addRule(/[0-9]/.test(password), "Contient un chiffre");
  addRule(/[!@#$%^&*(),.?\":{}|<>]/.test(password), "Contient un symbole");

  if (score <= 2) {
    strength.textContent = "Faible ❌";
    strength.style.color = "red";
  } 
  else if (score <= 4) {
    strength.textContent = "Moyen ⚠️";
    strength.style.color = "orange";
  } 
  else {
    strength.textContent = "Fort ✅";
    strength.style.color = "lightgreen";
  }
}