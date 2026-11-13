document.addEventListener("click", (event) => {
    const addCriterion = event.target.closest("[data-criteria-add]");
    if (addCriterion) {
        const section = addCriterion.closest("[data-criteria-section]");
        const template = section?.querySelector("[data-criterion-template]");
        const list = section?.querySelector("[data-criteria-list]");
        if (template && list) {
            list.append(template.content.cloneNode(true));
            renumberCriteria(list);
        }
        return;
    }

    const removeCriterion = event.target.closest("[data-criteria-remove]");
    if (removeCriterion) {
        const row = removeCriterion.closest("[data-criterion-row]");
        const list = row?.parentElement;
        row?.remove();
        if (list) {
            renumberCriteria(list);
        }
        return;
    }

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

function renumberCriteria(list) {
    list.querySelectorAll("[data-criterion-row]").forEach((row, index) => {
        const title = row.querySelector(".criterion-row__heading strong");
        if (title) {
            title.textContent = `Critério ${index + 1}`;
        }
    });
}

function updateRiceScore(dialog) {
    const output = dialog.querySelector("[data-rice-score]");
    if (!output) {
        return;
    }

    const pointsInput = dialog.querySelector('[name="story_points"]:checked');
    const effortInput = dialog.querySelector('[name="rice_effort"]');
    const effort = pointsInput ? Number(pointsInput.value) : null;
    if (effortInput) {
        effortInput.value = effort === null ? "" : String(effort);
    }

    const inputs = ["rice_reach", "rice_impact", "rice_confidence"]
        .map((name) => dialog.querySelector(`[name="${name}"]`));
    if (effort === null || inputs.some((input) => !input || !input.value.trim())) {
        output.textContent = "—";
        return;
    }
    const values = inputs.map((input) => Number(input.value));

    if (values.some((value) => !Number.isFinite(value)) || effort <= 0) {
        output.textContent = "—";
        return;
    }

    const score = (values[0] * values[1] * (values[2] / 100)) / effort;
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

document.addEventListener("change", (event) => {
    if (event.target.matches("[name='story_points']")) {
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
