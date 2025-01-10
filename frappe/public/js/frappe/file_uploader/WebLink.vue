<template>
	<div class="file-web-link margin-bottom">
<<<<<<< HEAD
		<a href class="text-muted text-medium" @click.prevent="$emit('hide-web-link')">
=======
		<a href class="text-muted text-medium" @click.prevent="emit('hide-web-link')">
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
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
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
</script>

<style scoped>
.file-web-link .input-group {
	margin-top: 10px;
}
</style>
