<template>
	<svg :height="radius * 2" :width="radius * 2">
		<circle
			:stroke-dasharray="circumference + ' ' + circumference"
			:style="{
				stroke: secondary,
				strokeDashoffset: 0,
			}"
			:stroke-width="stroke"
			fill="transparent"
			:r="normalizedRadius"
			:cx="radius"
			:cy="radius"
		/>
		<circle
			:stroke-dasharray="circumference + ' ' + circumference"
			:style="{
				stroke: primary,
				strokeDashoffset: strokeDashoffset,
			}"
			:stroke-width="stroke"
			fill="transparent"
			:r="normalizedRadius"
			:cx="radius"
			:cy="radius"
		/>
		<text
			dominant-baseline="middle"
			text-anchor="middle"
			:x="radius"
			:y="radius"
			:style="{
				color: 'var(--text-color)',
				fontSize: 'var(--text-xs)',
				fontWeight: 'var(--text-bold)',
			}"
		>
			{{ progress }}%
		</text>
	</svg>
</template>
<<<<<<< HEAD
<script>
export default {
	name: "ProgressRing",
	props: {
		primary: String,
		secondary: String,
		radius: Number,
		progress: Number,
		stroke: Number,
	},
	data() {
		const normalizedRadius = this.radius - this.stroke * 2;
		const circumference = normalizedRadius * 2 * Math.PI;

		return {
			normalizedRadius,
			circumference,
		};
	},
	computed: {
		strokeDashoffset() {
			return this.circumference - (this.progress / 100) * this.circumference;
		},
	},
};
=======

<script setup>
import { computed, ref } from "vue";

// props
const props = defineProps({
	primary: String,
	secondary: String,
	radius: Number,
	progress: Number,
	stroke: Number,
});

// variables
let normalizedRadius = ref(props.radius - props.stroke * 2);
let circumference = ref(normalizedRadius.value * 2 * Math.PI);

// computed
let strokeDashoffset = computed(() => {
	return circumference.value - (props.progress / 100) * circumference.value;
});
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
</script>

<style scoped>
circle {
	transition: stroke-dashoffset 0.35s;
	transform: rotate(-90deg);
	transform-origin: 50% 50%;
}
</style>
