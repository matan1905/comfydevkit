import { app } from "../../scripts/app.js";

const ext = {
	// Unique name for the extension
	name: "ComfyDevKit",
	async setup(app) {
		const menuLoadDefault = document.querySelector("#comfy-load-default-button");
		const devKitBtn = document.createElement("button");
		devKitBtn.textContent = "DevKit";
		devKitBtn.addEventListener("click", ()=>{
			window.onDevKitClick()
		})
		menuLoadDefault.after(devKitBtn);
	},
};

app.registerExtension(ext);

