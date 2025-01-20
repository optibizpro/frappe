<template>
	<div class="file-web-link margin-bottom">
<<<<<<< HEAD
		<a href class="text-muted text-medium" @click.prevent="$emit('hide-web-link')">
=======
		<a href class="text-muted text-medium" @click.prevent="emit('hide-web-link')">
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			{{ __("← Back to upload files") }}
		</a>
		<div class="input-group">
			<input
				type="text"
				class="form-control"
				:placeholder="__('Attach a web link')"
				v-model="url"
			/>
		</div>
	</div>
</template>
<<<<<<< HEAD
<script>
export default {
	name: "WebLink",
	data() {
		return {
			url: "",
		};
	},
};
=======

<script setup>
import { ref } from "vue";

// emits
let emit = defineEmits(["hide-web-link"]);

let url = ref("");

defineExpose({ url });
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
</script>

<style scoped>
.file-web-link .input-group {
	margin-top: 10px;
}
</style>
