<template>
	<div v-if="is_shown" class="flex justify-between build-success-message align-center">
		Compiled successfully
		<a v-if="!live_reload" class="ml-4 text-white underline" href="/" @click.prevent="reload">
			Refresh
		</a>
	</div>
</template>

<<<<<<< HEAD
			this.is_shown = true;
			if (this.timeout) {
				clearTimeout(this.timeout);
			}
			this.timeout = setTimeout(() => {
				this.hide();
			}, 10000);
		},
		hide() {
			this.is_shown = false;
		},
		reload() {
			window.location.reload();
		},
	},
};
=======
<script setup>
import { ref } from "vue";

// variables
let is_shown = ref(false);
let live_reload = ref(false);
let timeout = ref(null);

// Methods
function show(data) {
	if (data.live_reload) {
		live_reload.value = true;
		reload();
	}

	is_shown.value = true;
	if (timeout.value) {
		clearTimeout(timeout.value);
	}
	timeout.value = setTimeout(() => {
		hide();
	}, 10000);
}
function hide() {
	is_shown.value = false;
}
function reload() {
	window.location.reload();
}

defineExpose({ show, hide });
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
.build-success-message {
	position: fixed;
	z-index: 9999;
	bottom: 0;
	right: 0;
	background: rgba(0, 0, 0, 0.6);
	border-radius: var(--border-radius);
	padding: 0.5rem 1rem;
	color: white;
	font-weight: 500;
	margin: 1rem;
}
</style>
