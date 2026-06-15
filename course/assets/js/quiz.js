/**
 * quiz.js — interactive, single-page, closed-notes-style quiz.
 *
 * Usage: include a <script type="application/json" id="quiz-data"> in a page
 * with the shape:
 * {
 *   "title": "Week 1 Quiz — Track A",
 *   "track": "A",
 *   "week": 1,
 *   "time_limit_min": 15,
 *   "shuffle": true,
 *   "no_backtrack": true,
 *   "passing_pct": 70,
 *   "questions": [
 *     {"q": "...", "options": ["A","B","C","D"], "answer": 1, "level": "easy"},
 *     ...
 *   ]
 * }
 *
 * Then call: <div id="quiz-root"></div> and on DOM-ready the script renders.
 *
 * The score is computed in-browser. There's no server submit; the student is
 * asked to enter their score on a Google Form linked from the rubric (honor system,
 * but the timer + no-backtrack make it functionally close to closed-notes).
 */
(function () {
  function shuffle(arr) {
    var out = arr.slice();
    for (var i = out.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = out[i]; out[i] = out[j]; out[j] = tmp;
    }
    return out;
  }
  function el(tag, attrs, children) {
    var e = document.createElement(tag);
    for (var k in (attrs || {})) {
      if (k === "class") e.className = attrs[k];
      else if (k === "html") e.innerHTML = attrs[k];
      else if (k === "text") e.textContent = attrs[k];
      else e.setAttribute(k, attrs[k]);
    }
    (children || []).forEach(function (c) { if (c) e.appendChild(c); });
    return e;
  }

  document.addEventListener("DOMContentLoaded", function () {
    var dataEl = document.getElementById("quiz-data");
    var root = document.getElementById("quiz-root");
    if (!dataEl || !root) return;

    var quiz = JSON.parse(dataEl.textContent);
    var timeLimit = (quiz.time_limit_min || 15) * 60;
    var passing = quiz.passing_pct || 70;
    var noBack = quiz.no_backtrack !== false;

    // Prep questions: optionally shuffle (preserve answer index by tagging)
    var questions = (quiz.questions || []).map(function (q, idx) {
      var pairs = q.options.map(function (opt, i) {
        return { text: opt, correct: i === q.answer };
      });
      var shuffled = quiz.shuffle ? shuffle(pairs) : pairs;
      return {
        q: q.q, level: q.level || "easy",
        options: shuffled,
        idx: idx
      };
    });
    if (quiz.shuffle) questions = shuffle(questions);

    var state = {
      cur: 0,
      answers: new Array(questions.length).fill(null),
      done: false,
      startedAt: null,
      remaining: timeLimit
    };

    // Header
    var header = el("div", { class: "quiz-header" }, [
      el("h2", { text: quiz.title }),
      el("span", { class: "quiz-timer", id: "quiz-timer", text: "—:—" })
    ]);
    root.appendChild(header);

    var meta = el("div", {}, [
      el("p", {
        html: '<strong>Time limit:</strong> ' + (quiz.time_limit_min || 15) +
              ' min &middot; <strong>Pass:</strong> ≥' + passing +
              '% &middot; <strong>No backtracking:</strong> ' + (noBack ? "yes" : "no") +
              ' &middot; <strong>Questions:</strong> ' + questions.length +
              '. <em>This is closed-notes.</em>'
      })
    ]);
    root.appendChild(meta);

    var startBtn = el("button", { class: "md-button md-button--primary", text: "▶ Start the quiz" });
    var startBox = el("div", {}, [startBtn]);
    root.appendChild(startBox);

    var qContainer = el("div", { id: "quiz-questions" });
    root.appendChild(qContainer);

    var actions = el("div", { class: "quiz-actions" });
    root.appendChild(actions);

    var resultBox = el("div", { id: "quiz-result", class: "quiz-result" });
    root.appendChild(resultBox);

    function renderQuestion(i) {
      qContainer.innerHTML = "";
      var q = questions[i];
      var qEl = el("div", { class: "quiz-question" }, [
        el("p", {
          html: "<strong>Q" + (i + 1) + " / " + questions.length + ".</strong> " + q.q +
            ' <span class="level ' + q.level + '">' + q.level + "</span>"
        })
      ]);
      q.options.forEach(function (opt, oi) {
        var label = el("label", { for: "q" + i + "o" + oi });
        var radio = el("input", { type: "radio", name: "q" + i, id: "q" + i + "o" + oi, value: String(oi) });
        if (state.answers[i] && state.answers[i].pickedIdx === oi) radio.checked = true;
        radio.addEventListener("change", function () {
          state.answers[i] = { pickedIdx: oi, correct: opt.correct };
        });
        label.appendChild(radio);
        label.appendChild(document.createTextNode(" " + opt.text));
        qEl.appendChild(label);
      });
      qContainer.appendChild(qEl);

      // Actions
      actions.innerHTML = "";
      if (!noBack && i > 0) {
        var prev = el("button", { class: "md-button", text: "← Back" });
        prev.addEventListener("click", function () { state.cur--; renderQuestion(state.cur); });
        actions.appendChild(prev);
      }
      if (i < questions.length - 1) {
        var next = el("button", { class: "md-button md-button--primary", text: "Next →" });
        next.addEventListener("click", function () {
          if (!state.answers[i]) { alert("Pick an answer first."); return; }
          state.cur++; renderQuestion(state.cur);
        });
        actions.appendChild(next);
      } else {
        var submit = el("button", { class: "md-button md-button--primary", text: "Submit" });
        submit.addEventListener("click", function () {
          if (!state.answers[i]) { alert("Pick an answer first."); return; }
          finish();
        });
        actions.appendChild(submit);
      }
    }

    function tick() {
      if (state.done) return;
      state.remaining -= 1;
      var t = document.getElementById("quiz-timer");
      var m = Math.floor(Math.max(0, state.remaining) / 60);
      var s = Math.max(0, state.remaining) % 60;
      t.textContent = m + ":" + (s < 10 ? "0" + s : s);
      t.classList.remove("warn", "over");
      if (state.remaining <= 60) t.classList.add("warn");
      if (state.remaining <= 0) { t.classList.add("over"); finish(true); return; }
      setTimeout(tick, 1000);
    }

    function finish(timeUp) {
      state.done = true;
      var correct = state.answers.filter(function (a) { return a && a.correct; }).length;
      var pct = Math.round(100 * correct / questions.length);
      var earnings = pct >= passing ? 1.0 : (pct >= 50 ? 0.5 : 0.0);
      qContainer.innerHTML = "";
      actions.innerHTML = "";

      // Show review
      questions.forEach(function (q, i) {
        var ans = state.answers[i];
        var row = el("div", { class: "quiz-question" }, [
          el("p", {
            html: "<strong>Q" + (i + 1) + ".</strong> " + q.q +
                  ' <span class="level ' + q.level + '">' + q.level + "</span>"
          })
        ]);
        q.options.forEach(function (opt, oi) {
          var cls = "";
          if (opt.correct) cls = "correct";
          else if (ans && ans.pickedIdx === oi) cls = "wrong";
          row.appendChild(el("label", { class: cls, text: " " + opt.text + (opt.correct ? "  ✓" : "") }));
        });
        qContainer.appendChild(row);
      });

      var cls = pct >= passing ? "passed" : (pct >= 50 ? "partial" : "failed");
      resultBox.className = "quiz-result " + cls;
      resultBox.innerHTML =
        (timeUp ? "<strong>⏰ Time's up.</strong> " : "") +
        "Score: <strong>" + correct + " / " + questions.length + " (" + pct + "%)</strong>" +
        " &mdash; estimated wallet earning: <strong>$" + earnings.toFixed(2) + "</strong>" +
        (pct >= passing ? " 🎉" : (pct >= 50 ? " (partial credit)" : "")) +
        '<br><br><a class="md-button" href="' +
        (quiz.submit_url || "#submit") +
        '" target="_blank" rel="noopener">📨 Report your score to the instructor</a>';
    }

    startBtn.addEventListener("click", function () {
      startBox.style.display = "none";
      state.startedAt = new Date();
      tick();
      renderQuestion(0);
    });
  });
})();
