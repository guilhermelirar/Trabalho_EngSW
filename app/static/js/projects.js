document.addEventListener("click", (event) => {
    const tab = event.target.closest("[data-tab-target]");
    if (tab) {
        const tabs = tab.closest(".project-tabs");
        const panel = document.getElementById(tab.dataset.tabTarget);
        if (tabs && panel) {
            tabs.querySelectorAll("[role='tab']").forEach((item) => {
                const isActive = item === tab;
                item.classList.toggle("is-active", isActive);
                item.setAttribute("aria-selected", String(isActive));
                document.getElementById(item.dataset.tabTarget).hidden = !isActive;
            });
        }
        return;
    }

    const opener = event.target.closest("[data-dialog-open]");
    if (opener) {
        const dialogId = opener.dataset.dialogOpen;
        const dialog = document.getElementById(dialogId);
        if (dialog) {
            if (dialogId === "new-story-dialog") {
                const sprintId = opener.dataset.sprintId || "";
                const sprintInput = dialog.querySelector("input[name='sprint_backlog_id']");
                if (sprintInput) {
                    sprintInput.value = sprintId;
                }
            }
            updateRiceScore(dialog);
            dialog.showModal();
        }
        return;
    }

    const closer = event.target.closest("[data-dialog-close]");
    if (closer) {
        closer.closest("dialog")?.close();
    }
});

function updateRiceScore(dialog) {
    const output = dialog.querySelector("[data-rice-score]");
    if (!output) {
        return;
    }

    const inputs = ["rice_reach", "rice_impact", "rice_confidence", "rice_effort"]
        .map((name) => dialog.querySelector(`[name="${name}"]`));
    if (inputs.some((input) => !input || !input.value.trim())) {
        output.textContent = "—";
        return;
    }
    const values = inputs.map((input) => Number(input.value));

    if (values.some((value) => !Number.isFinite(value)) || values[3] <= 0) {
        output.textContent = "—";
        return;
    }

    const score = (values[0] * values[1] * (values[2] / 100)) / values[3];
    output.textContent = Number.isInteger(score) ? String(score) : score.toFixed(2);
}

document.addEventListener("input", (event) => {
    if (event.target.matches("[data-rice-field]")) {
        const dialog = event.target.closest("dialog");
        if (dialog) {
            updateRiceScore(dialog);
        }
    }
});

document.querySelectorAll("dialog").forEach((dialog) => {
    dialog.addEventListener("click", (event) => {
        if (event.target === dialog) {
            dialog.close();
        }
    });
});

document.addEventListener("submit", (event) => {
    const message = event.target.dataset.confirm || event.submitter?.dataset.confirm;
    if (message && !window.confirm(message)) {
        event.preventDefault();
    }
});
