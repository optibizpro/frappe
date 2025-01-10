<template>
	<div>
		<p class="mb-3 text-muted">
			{{ help_message }}
		</p>
		<div class="row font-weight-bold">
			<div class="col-8">
				{{ __("Column") }}
			</div>
			<div class="col-4">
				{{ __("Width") }}
				({{ __("Total:") }} {{ total_width }})
			</div>
		</div>
		<draggable
			:list="df.table_columns"
			:animation="200"
			:group="df.fieldname"
			handle=".icon-drag"
		>
<<<<<<< HEAD
			<div class="mt-2 row align-center column-row" v-for="column in df.table_columns">
				<div class="col-8">
					<div class="column-label d-flex align-center">
						<div class="px-2 icon-drag ml-n2">
							<svg class="icon icon-xs">
								<use href="#icon-drag"></use>
							</svg>
						</div>
						<div class="mt-1 ml-1">
							<input
								class="input-column-label"
								:class="{ 'text-danger': column.invalid_width }"
								type="text"
								v-model="column.label"
							/>
=======
			<template #item="{ element: column }">
				<div class="mt-2 row align-center column-row">
					<div class="col-8">
						<div class="column-label d-flex align-center">
							<div class="px-2 icon-drag ml-n2">
								<svg class="icon icon-xs">
									<use href="#icon-drag"></use>
								</svg>
							</div>
							<div class="mt-1 ml-1">
								<input
									class="input-column-label"
									:class="{ 'text-danger': column.invalid_width }"
									type="text"
									v-model="column.label"
								/>
							</div>
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
						</div>
					</div>
					<div class="col-4 d-flex align-items-center">
						<input
							type="number"
							class="text-right form-control"
							:class="{ 'text-danger is-invalid': column.invalid_width }"
							v-model.number="column.width"
							min="0"
							max="100"
							step="5"
						/>
						<button class="ml-2 btn btn-xs btn-icon" @click="remove_column(column)">
							<svg class="icon icon-sm">
								<use href="#icon-close"></use>
							</svg>
						</button>
					</div>
				</div>
<<<<<<< HEAD
				<div class="col-4 d-flex align-items-center">
					<input
						type="number"
						class="text-right form-control"
						:class="{ 'text-danger is-invalid': column.invalid_width }"
						v-model.number="column.width"
						min="0"
						max="100"
						step="5"
					/>
					<button class="ml-2 btn btn-xs btn-icon" @click="remove_column(column)">
						<svg class="icon icon-sm">
							<use href="#icon-close"></use>
						</svg>
					</button>
				</div>
			</div>
=======
			</template>
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		</draggable>
	</div>
</template>

<script setup>
import { computed } from "vue";
import draggable from "vuedraggable";
<<<<<<< HEAD
export default {
	name: "ConfigureColumns",
	props: ["df"],
	components: {
		draggable,
	},
	methods: {
		remove_column(column) {
			this.$set(
				this.df,
				"table_columns",
				this.df.table_columns.filter((_column) => _column !== column)
			);
		},
	},
	computed: {
		help_message() {
			// prettier-ignore
			return __("Drag columns to set order. Column width is set in percentage. The total width should not be more than 100. Columns marked in red will be removed.");
		},
		total_width() {
			return this.df.table_columns.reduce((total, tf) => total + tf.width, 0);
		},
	},
};
=======

// props
const props = defineProps(["df"]);

// methods
function remove_column(column) {
	props.df["table_columns"] = props.df.table_columns.filter((_column) => _column !== column);
}
// computed
let help_message = computed(() => {
	// prettier-ignore
	return __("Drag columns to set order. Column width is set in percentage. The total width should not be more than 100. Columns marked in red will be removed.");
});
let total_width = computed(() => {
	return props.df.table_columns.reduce((total, tf) => total + tf.width, 0);
});
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
</script>

<style scoped>
.icon-drag {
	cursor: grab;
}
.input-column-label {
	border: 1px solid transparent;
	border-radius: var(--border-radius);
	font-size: var(--text-md);
}
.input-column-label:focus {
	border-color: var(--border-color);
	outline: none;
	background-color: var(--control-bg);
}
.input-column-label::placeholder {
	font-style: italic;
	font-weight: normal;
}
</style>
