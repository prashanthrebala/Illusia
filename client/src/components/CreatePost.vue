<template>
	<div class="w-full flex justify-center gap-3">
		<input
			ref="inputField"
			type="text"
			placeholder="Enter a prompt..."
			class="max-w-[32rem] w-5/6 rounded-lg px-4 p-2 outline-0 h-12 md:h-14 border-2 border-neutral-600 bg-slate-100 text-neutral-800"
		/>
		<button
			class="bg-neutral-950 w-24 p-2 text-white rounded-lg flex justify-center items-center"
			@click="createPost"
			:disabled="isLoading"
		>
			<span v-if="isLoading">Creating...</span>
			<span v-else>Create!</span>
		</button>
	</div>
	<div
		v-if="isLoading"
		class="w-full h-24 flex justify-center items-center text-xs"
	>
		Loading...
	</div>
	<div
		v-else-if="error"
		class="w-full h-24 flex justify-center items-center text-xs text-red-500"
	>
		{{ error }}
	</div>
	<div v-else-if="imageUrl" class="w-full flex justify-center p-8">
		<div
			id="image"
			class="max-w-[24rem] w-full aspect-square bg-cover bg-center"
			:style="{ 'background-image': `url(${imageUrl})` }"
		/>
	</div>
	<div class="w-full h-24 flex justify-center items-center text-xs">
		Note that the image generated will automatically be visible to everyone who
		uses this website
	</div>
</template>

<script>
export default {
	data() {
		return {
			imageUrl: "", // Initialize imageUrl
			isLoading: false,
			error: "",
		};
	},
	methods: {
		async createPost() {
			const inputFieldValue = this.$refs.inputField.value; // Get the value from the input field

			this.isLoading = true;
			this.error = "";

			const apiUrl = "http://localhost:8001/images/create"; // Replace with your API URL
			const requestData = {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					prompt: inputFieldValue,
				}),
			};

			try {
				const response = await fetch(apiUrl, requestData);
				if (!response.ok) {
					throw new Error("Network response was not ok");
				}
				const responseData = await response.json();
				this.imageUrl = responseData.imageUrl; // Update imageUrl
				console.log("Post created successfully");
			} catch (error) {
				console.error("Error creating post:", error);
				this.error = "Error creating post. Please try again.";
			} finally {
				this.isLoading = false;
			}
		},
	},
};
</script>
