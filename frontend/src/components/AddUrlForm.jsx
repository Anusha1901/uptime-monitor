import { useState } from "react";
import api from "../services/api";

function AddUrlForm({ onUrlAdded }) {
    const [url, setUrl] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleSubmit(event) {
        event.preventDefault();

        if (!url.trim()) return;

        try {
            setLoading(true);

            await api.post("/urls", {
                url,
            });

            setUrl("");

            onUrlAdded();

        } catch (error) {

            if (error.response?.status === 400) {
                alert("URL already exists.");
            } else {
                alert("Unable to add URL.");
            }

        } finally {
            setLoading(false);
        }
    }

    return (
        <form className="url-form" onSubmit={handleSubmit}>

            <input
                type="url"
                placeholder="https://example.com"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                required
            />

            <button type="submit" disabled={loading}>
                {loading ? "Adding..." : "Add URL"}
            </button>

        </form>
    );
}

export default AddUrlForm;