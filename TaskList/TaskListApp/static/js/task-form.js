/**
 * Task Form Management
 * Manages the main task input form and its interactions
 */

// Element references
const taskInput = document.getElementById('taskInput');
const okBtn = document.getElementById('okBtn');
const cancelBtn = document.getElementById('cancelBtn');
const taskForm = document.getElementById('taskForm');
const leftButtonsContainer = document.getElementById('leftButtons');
const leftButtons = document.querySelectorAll('#extraButtons button');
const plusToggle = document.getElementById('plusToggle');
const mobileActionBtn = document.getElementById('mobileActionBtn');


//Updates button states based on input content and screen size

function updateButtons() {
  const isEmpty = taskInput.value.trim() === "";
  const isMobile = window.innerWidth < 1230;

  if (isMobile) {
    mobileActionBtn.classList.remove('d-none');
    cancelBtn.classList.add('d-none');
    okBtn.classList.add('d-none');
    mobileActionBtn.innerHTML = `<i data-feather="${isEmpty ? 'x' : 'plus'}"></i>`;
    feather.replace();
  } else {
    mobileActionBtn.classList.add('d-none');
    cancelBtn.classList.remove('d-none');
    okBtn.classList.remove('d-none');
    okBtn.textContent = isEmpty ? "Ok" : "Add";
    cancelBtn.disabled = false;
  }

  leftButtons.forEach(btn => btn.disabled = isEmpty);
}

// Event Listeners
taskInput.addEventListener('input', updateButtons);
window.addEventListener('resize', updateButtons);

taskInput.addEventListener('focus', () => leftButtonsContainer.classList.add('show'));
taskInput.addEventListener('blur', () => setTimeout(() => {
  if (taskInput.value.trim() === "") {
    leftButtonsContainer.classList.remove('show');
  }
}, 100));

cancelBtn.addEventListener('click', () => {
  taskInput.value = "";
  okBtn.textContent = "Ok";
  cancelBtn.disabled = false;
  leftButtons.forEach(btn => btn.disabled = true);
  leftButtonsContainer.classList.remove('show');
});

taskForm.addEventListener('submit', (e) => {
  if (taskInput.value.trim() === "") e.preventDefault();
});

plusToggle.addEventListener('click', () => {
  if (!leftButtonsContainer.classList.contains('show')) {
    leftButtonsContainer.classList.add('show');
    taskInput.focus();
  }
});

mobileActionBtn.addEventListener('click', () => {
  const isEmpty = taskInput.value.trim() === "";
  if (isEmpty) {
    taskInput.value = "";
    leftButtonsContainer.classList.remove('show');
    updateButtons();
  } else {
    taskForm.submit();
  }
});

// Initialize UI
document.addEventListener('DOMContentLoaded', () => {
  updateButtons();
});