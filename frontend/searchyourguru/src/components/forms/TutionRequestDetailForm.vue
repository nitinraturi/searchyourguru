<template>
    <div>
        <form
            action="#"
            method="POST"
            v-on:submit.prevent="student_additional_details"
        >
        <div class="columns is-multiline">
            <div class="column is-full">
                <div class="field">
                    <label class="label">Mobile</label>
                    <div class="control">
                        <input
                            type="text"
                            class="input"
                            placeholder="Eg: 9810141414"
                            v-model="student_mobile"
                            required
                        />
                    </div>
                </div>
            </div>
            <div class="column is-full">
                <div class="field">
                    <label class="label">Address</label>
                    <div class="control">
                        <textarea
                            class="textarea"
                            placeholder="Eg: krishna nagar delhi 110051"
                            v-model="student_address"
                            required
                        ></textarea>
                    </div>
                </div>
            </div>
            <div class="column is-full">
                <button
                    type="submit"
                    class="button is-link is-outlined"
                    v-on:submit.prevent="student_additional_details"
                >
                    Save Details
                </button>
            </div>
        </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'TutionRequestDetailForm',
        data: function() {
            return {
                student_mobile: null,
                student_address: null
            }
        },
        methods: {
            student_additional_details: function() {
                this.$emit("studentAdditionalDetails", {
                    mobile: this.student_mobile,
                    address: this.student_address
                })
            }
        }
    }
</script>