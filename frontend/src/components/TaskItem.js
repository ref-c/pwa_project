import React, { useState } from "react";
const TaskItem = ({ task, deleteTask }) => {
    const [isCompleted, setIsCompleted] = useState(task.completed);
    const toggleComplete = () => {
        // Toggle completion status
        setIsCompleted(!isCompleted);
    };
    return (
        <li className={`task-item ${isCompleted ? "completed" : ""}`}>
            <input
                type="checkbox"
                checked={isCompleted}
                onChange={toggleComplete}
            />
            <span className="task-name">{task.name}</span>
            <button onClick={() => deleteTask(task.id)} className="delete-btn">
                ✕
            </button>
        </li>
    );
};
export default TaskItem;