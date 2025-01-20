<template>
	<div class="file-web-link margin-bottom">
<<<<<<< HEAD
		<a href class="text-muted text-medium" @click.prevent="$emit('hide-web-link')">
=======
		<a href class="text-muted text-medium" @click.prevent="emit('hide-web-link')">
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
</script>

<style scoped>
.file-web-link .input-group {
	margin-top: 10px;
}
</style>
