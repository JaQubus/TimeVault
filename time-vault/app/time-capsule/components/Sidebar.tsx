import React from "react";
import styles from "../styles.module.scss";

export default function Sidebar() {
  return (
    <aside className={styles.sidebar}>
        <a href="/time-capsule">
            <div className={styles.logo_container}>
                <img src="logo.png" alt="Logo" />
            </div>
        </a>

<div className={styles.sidebar_items}>
    <a className={styles.sidebar_item} href="/time-capsule">
        <img src="bx-hourglass.png" alt="Icon" />
        <span>Time Capsule</span>
    </a>
    <a className={styles.sidebar_item}>
        <img src="bx-calendar-star.png" alt="Icon" />
        <span>Goals</span>
    </a>
    <a className={styles.sidebar_item}>
        <img src="bx-question-mark.png" alt="Icon" />
        <span>Questions</span>
    </a>
    <a className={styles.sidebar_item} href="/photos-timeline">
        <img src="bxs-photo-album.png" alt="Icon" />
        <span>Photos timeline</span>
    </a>
</div>
<div className={styles.sidebar_footer}>
    <div className={styles.sidebar_footer_account}>
        <img src="bxs-user-rectangle.png" alt="user-icon"></img>
        <span>Username</span>
    </div>
    <button className={styles.sidebar_button}>Logout</button>
</div>
</aside>
);
}