/**
 * Task Inline Editor
 * Manages inline editing functionality for existing tasks
 */

let activeInlineEditor = null;

/**
 * Attaches click event to task items to enable inline editing
 * @param {HTMLElement} span - The task span element
 */
function attachEditListener(span) {
  span.addEventListener('click', () => {
    if (activeInlineEditor) {
      activeInlineEditor.replaceWith(activeInlineEditor.originalSpan);
      activeInlineEditor = null;
    }

    const taskText = span.textContent.trim();
    const taskId = span.getAttribute('data-id');

    const editor = document.createElement('div');
    editor.classList.add('task-box', 'inline-editor', 'mt-2');

    const csrfToken = document.getElementById('csrf-token').innerHTML;

    editor.innerHTML = createEditorHTML(taskText, taskId, csrfToken);
    feather.replace();

    span.replaceWith(editor);
    editor.originalSpan = span;
    activeInlineEditor = editor;

    // Focus the input and position cursor at end
    const input = editor.querySelector('input[name="title"]');
    setTimeout(() => {
      input.focus();
      input.setSelectionRange(input.value.length, input.value.length);
      feather.replace();
    }, 0);

    setupEditorEvents(editor, span);
  });
}


//Creates HTML for the inline editor

function createEditorHTML(taskText, taskId, csrfToken) {
  return `
    <form method="post" action="/add-task/" class="inline-edit-form">
      ${csrfToken}
      <input type="hidden" name="task_id" value="${taskId}">
      <div class="input-wrapper">
        <input type="text" name="title" class="form-control task-input ps-5" value="${taskText}" autofocus>
      </div>
      <div class="task-buttons d-flex justify-content-between align-items-center flex-nowrap gap-2 mt-2">
        <div class="d-flex gap-2 overflow-auto extraButtons">
          <button type="button" class="task-button" disabled><i data-feather="maximize-2"></i> Open</button>
          <button type="button" class="task-button" disabled><i data-feather="calendar"></i> Today</button>
          <button type="button" class="task-button" disabled><i data-feather="lock"></i> Public</button>
          <button type="button" class="task-button" disabled><i data-feather="sun"></i> Highlight</button>
          <button type="button" class="task-button" disabled><i data-feather="circle"></i> Estimation</button>
        </div>
        <div class="btn-group-right d-flex gap-2">
          <button type="button" class="task-button btn-cancel-inline">Cancel</button>
          <button type="submit" class="task-button btn-ok-inline">Save</button>
          <button type="button" class="task-button d-none btn-mobile-inline"><i data-feather="save"></i></button>
        </div>
      </div>
    </form>
  `;
}


//Sets up event listeners for the inline editor

function setupEditorEvents(editor, originalSpan) {
  const input = editor.querySelector('input[name="title"]');
  const cancelBtn = editor.querySelector('.btn-cancel-inline');
  const okBtn = editor.querySelector('.btn-ok-inline');
  const mobileBtn = editor.querySelector('.btn-mobile-inline');
  const extras = editor.querySelectorAll('.extraButtons button');

  function updateInlineButtons() {
    const isEmpty = input.value.trim() === "";
    const isMobile = window.innerWidth < 1230;

    if (isMobile) {
      cancelBtn.classList.add('d-none');
      okBtn.classList.add('d-none');
      mobileBtn.classList.remove('d-none');
      mobileBtn.innerHTML = `<i data-feather="${isEmpty ? 'x' : 'save'}"></i>`;
      feather.replace();
    } else {
      cancelBtn.classList.remove('d-none');
      okBtn.classList.remove('d-none');
      mobileBtn.classList.add('d-none');
    }

    extras.forEach(btn => btn.disabled = isEmpty);
  }

  input.addEventListener('input', updateInlineButtons);
  window.addEventListener('resize', updateInlineButtons);
  updateInlineButtons();

  cancelBtn.addEventListener('click', () => {
    editor.replaceWith(originalSpan);
    attachEditListener(originalSpan);
    activeInlineEditor = null;
  });

  mobileBtn.addEventListener('click', () => {
    const isEmpty = input.value.trim() === "";
    if (isEmpty) {
      editor.replaceWith(originalSpan);
      attachEditListener(originalSpan);
      activeInlineEditor = null;
    } else {
      editor.querySelector('form').submit();
    }
  });
}


//Close inline editor when clicking outside

document.addEventListener('click', (e) => {
  if (
    activeInlineEditor &&
    !activeInlineEditor.contains(e.target) &&
    !e.target.classList.contains('editable-task')
  ) {
    const originalSpan = activeInlineEditor.originalSpan;
    activeInlineEditor.replaceWith(originalSpan);
    attachEditListener(originalSpan);
    activeInlineEditor = null;
  }
});


//Initialize the editor

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.editable-task').forEach(attachEditListener);
});