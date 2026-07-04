function StatusBadge({ status }) {
    const isUp = status === "UP";

    return (
        <span
            style={{
                backgroundColor: isUp ? "#d4edda" : "#f8d7da",
                color: isUp ? "#155724" : "#721c24",
                padding: "6px 12px",
                borderRadius: "20px",
                fontWeight: "bold",
                display: "inline-block",
                minWidth: "60px",
                textAlign: "center"
            }}
        >
            {isUp ? "🟢 UP" : "🔴 DOWN"}
        </span>
    );
}

export default StatusBadge;