let selectedModel = "stable-diffusion-v1-4";

function selectModel(model) {
  selectedModel = model;
  document.querySelectorAll(".model-button").forEach((btn) => {
    btn.style.backgroundColor = "";
  });

  document.querySelector(`button[onclick="selectModel('${model}')"]`).style.backgroundColor = "#4CAF50"; // Green color
}

document.getElementById("generate").onclick = async function () {
  const prompt = document.getElementById("prompt").value;

  if (!prompt) {
    alert("Please enter a prompt.");
    return;
  }

  // Show the loading spinner
  document.getElementById("loading-spinner").style.display = "flex";

  try {
    const response = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ model: selectedModel, prompt })
    });

    if (!response.ok) {
      throw new Error("Failed to generate image.");
    }

    const blob = await response.blob();
    const imgURL = URL.createObjectURL(blob);
    const imgElement = document.getElementById("generated-image");

    imgElement.src = imgURL;
    document.getElementById("download").style.display = "inline"; // Show download button
  } catch (error) {
    console.error(error);
    alert("Error generating image. Please try again.");
  } finally {
    // Hide the loading spinner after the process is complete
    document.getElementById("loading-spinner").style.display = "none";
  }
};

function downloadImage() {
  const imgElement = document.getElementById("generated-image");
  const link = document.createElement("a");

  link.href = imgElement.src;
  link.download = "generated_image.png";
  link.click();
}
