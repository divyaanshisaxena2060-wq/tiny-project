 const fileInput = document.getElementById("fileInput");
    const statusText = document.getElementById("statusText");

    dropzone.addEventListener("click", () => fileInput.click());

    fileInput.addEventListener("change", () => {
      const file = fileInput.files[0];
      if (file) {
        statusText.textContent = "Selected: " + file.name;
      }
    });

    ["dragenter", "dragover"].forEach(eventName => {
      dropzone.addEventListener(eventName, e => {
        e.preventDefault();
        dropzone.style.borderColor = "#4f46e5";
      });
    });

    ["dragleave", "drop"].forEach(eventName => {
      dropzone.addEventListener(eventName, e => {
        e.preventDefault();
        dropzone.style.borderColor = "#9aa8ff";
      });
    });

    dropzone.addEventListener("drop", e => {
      const files = e.dataTransfer.files;
      if (files.length > 0) {
        fileInput.files = files;
        statusText.textContent = "Selected: " + files[0].name;
      }
    });