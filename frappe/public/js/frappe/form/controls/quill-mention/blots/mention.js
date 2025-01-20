<<<<<<< HEAD
/* eslint-disable */
=======
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
import Quill from "quill";

const Embed = Quill.import("blots/embed");

class MentionBlot extends Embed {
	static create(data) {
		const node = super.create();
		const denotationChar = document.createElement("span");
		denotationChar.className = "ql-mention-denotation-char";
		denotationChar.innerHTML = data.denotationChar;
		node.appendChild(denotationChar);
		node.innerHTML += data.value;
		node.innerHTML += `${data.isGroup === "true" ? frappe.utils.icon("users") : ""}`;
		node.dataset.id = data.id;
		node.dataset.value = data.value;
		node.dataset.denotationChar = data.denotationChar;
		node.dataset.isGroup = data.isGroup;
		if (data.link) {
			node.dataset.link = data.link;
		}
		return node;
	}

	static value(domNode) {
		return {
			id: domNode.dataset.id,
			value: domNode.dataset.value,
			link: domNode.dataset.link || null,
			denotationChar: domNode.dataset.denotationChar,
			isGroup: domNode.dataset.isGroup,
		};
	}
}

MentionBlot.blotName = "mention";
MentionBlot.tagName = "span";
MentionBlot.className = "mention";

Quill.register(MentionBlot, true);
