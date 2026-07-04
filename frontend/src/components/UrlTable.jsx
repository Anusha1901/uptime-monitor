import StatusBadge from "./StatusBadge";

function UrlTable({ urls }) {

    if (urls.length === 0) {
        return <p>No URLs added yet.</p>;
    }

    return (
        <table className="url-table">
            <thead>
                <tr>
                    <th>URL</th>
                    <th>Status</th>
                    <th>Status Code</th>
                    <th>Response Time</th>
                    <th>Last Checked</th>
                </tr>
            </thead>

            <tbody>

                {urls.map((url) => (

                    <tr key={url.id}>

                        <td>{url.url}</td>

                        <td>
                            <StatusBadge status={url.status} />
                        </td>

                        <td>
                            {url.status_code ?? "-"}
                        </td>

                        <td>
                            {url.response_time != null
                                ? `${url.response_time} ms`
                                : "-"
                            }
                        </td>

                        <td>
                            {url.last_checked
                                ? new Date(url.last_checked).toLocaleString()
                                : "-"
                            }
                        </td>

                    </tr>

                ))}

            </tbody>
        </table>
    );
}

export default UrlTable;