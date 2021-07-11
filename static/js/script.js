const action_name = "action_greet_user";
const rasa_server_url = "http://localhost:5005/webhooks/rest/webhook";
const sender_id = uuidv4();
document.addEventListener("DOMContentLoaded", () => {
  const elemsTap = document.querySelector(".tap-target");
  const instancesTap = M.TapTarget.init(elemsTap, {});
  instancesTap.open();
  setTimeout(() => {
    instancesTap.close();
  }, 4000);
});

$(document).ready(() => {
  $("div").removeClass("tap-target-origin");

  $(".dropdown-trigger").dropdown();

  $(".modal").modal();

});


function scrollToBottomOfResults() {
  const terminalResultsDiv = document.getElementById("chats");
  terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight;
}


function hideBotTyping() {
  $("#botAvatar").remove();
  $(".botTyping").remove();
}


function showBotTyping() {
  const botTyping =
    '<img class="botAvatar" id="botAvatar" src="{% static 'images/sara_avatar.png' %}" /><div class="botTyping"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div>';
  $(botTyping).appendTo(".chats");
  $(".botTyping").show();
  scrollToBottomOfResults();
}


function setUserResponse(message) {
  const user_response = `<img class="userAvatar" src="{% static 'images/userAvatar.jpg' %}"' ><p class="userMsg">${message} </p><div class="clearfix"></div>`;
  $(user_response).appendTo(".chats").show("slow");

  $(".usrInput").val("");
  scrollToBottomOfResults();
  showBotTyping();
  $(".suggestions").remove();
}


function addSuggestion(suggestions) {
  setTimeout(() => {
    const suggLength = suggestions.length;
    $(
      ' <div class="singleCard"> <div class="suggestions"><div class="menu"></div></div></diV>'
    )
      .appendTo(".chats")
      .hide()
      .fadeIn(1000);
    
    for (let i = 0; i < suggLength; i += 1) {
      $(
        `<div class="menuChips" data-payload='${suggestions[i].payload}'>${suggestions[i].title}</div>`
      ).appendTo(".menu");
    }
    scrollToBottomOfResults();
  }, 1000);
}


function createCardsCarousel(cardsData) {
  let cards = "";
  for (let i = 0; i < cardsData.length; i += 1) {
    const title = cardsData[i].name;
    const ratings = `${Math.round((cardsData[i].ratings / 5) * 100)}%`;
    const item = `<div class="carousel_cards in-left">
    <img class="cardBackgroundImage" src="${cardsData[i].image}">
    <div class="cardFooter"> <span class="cardTitle" title="${title}">${title}</span>
    <div class="cardDescription"><div class="stars-outer">
    <div class="stars-inner" style="width:${ratings}" >
    </div></div></div></div></div>`;

    cards += item;
  }
  const cardContents = `<div id="paginated_cards" class="cards"> <div class="cards_scroller">${cards} <span class="arrow prev fa fa-chevron-circle-left "></span> <span class="arrow next fa fa-chevron-circle-right" ></span> </div> </div>`;
  return cardContents;
}


function showCardsCarousel(cardsToAdd) {
  const cards = createCardsCarousel(cardsToAdd);

  $(cards).appendTo(".chats").show();

  if (cardsToAdd.length <= 2) {
    $(`.cards_scroller>div.carousel_cards:nth-of-type(${i})`).fadeIn(3000);
  } else {
    for (let i = 0; i < cardsToAdd.length; i += 1) {
      $(`.cards_scroller>div.carousel_cards:nth-of-type(${i})`).fadeIn(3000);
    }
    $(".cards .arrow.prev").fadeIn("3000");
    $(".cards .arrow.next").fadeIn("3000");
  }

  scrollToBottomOfResults();

  const card = document.querySelector("#paginated_cards");
  const card_scroller = card.querySelector(".cards_scroller");
  const card_item_size = 225;

  function scrollToNextPage() {
    card_scroller.scrollBy(card_item_size, 0);
  }

  function scrollToPrevPage() {
    card_scroller.scrollBy(-card_item_size, 0);
  }

  card.querySelector(".arrow.next").addEventListener("click", scrollToNextPage);
  card.querySelector(".arrow.prev").addEventListener("click", scrollToPrevPage);
}


function showQuickReplies(quickRepliesData) {
  let chips = "";
  for (let i = 0; i < quickRepliesData.length; i += 1) {
    const chip = `<div class="chip" data-payload='${quickRepliesData[i].payload}'>${quickRepliesData[i].title}</div>`;
    chips += chip;
  }

  const quickReplies = `<div class="quickReplies">${chips}</div><div class="clearfix"></div>`;
  $(quickReplies).appendTo(".chats").fadeIn(1000);
  scrollToBottomOfResults();
  const slider = document.querySelector(".quickReplies");
  let isDown = false;
  let startX;
  let scrollLeft;

  slider.addEventListener("mousedown", (e) => {
    isDown = true;
    slider.classList.add("active");
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
  });
  slider.addEventListener("mouseleave", () => {
    isDown = false;
    slider.classList.remove("active");
  });
  slider.addEventListener("mouseup", () => {
    isDown = false;
    slider.classList.remove("active");
  });
  slider.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 3; // scroll-fast
    slider.scrollLeft = scrollLeft - walk;
  });
}


function renderPdfAttachment(pdf_data) {
  const { url: pdf_url } = pdf_data.custom;
  const { title: pdf_title } = pdf_data.custom;
  const pdf_attachment = `<div class="pdf_attachment"><div class="row"><div class="col s3 pdf_icon">
<i class="fa fa-file-pdf-o" aria-hidden="true"></i></div><div class="col s9 pdf_link"><a href="${pdf_url}" target="_blank">
${pdf_title} </a></div></div></div>`;

  $(".chats").append(pdf_attachment);
  scrollToBottomOfResults();
}


function renderDropDwon(drop_down_data) {
  let drop_down_options = "";
  for (let i = 0; i < drop_down_data.length; i += 1) {
    drop_down_options += `<option value="${drop_down_data[i].value}">${drop_down_data[i].label}</option>`;
  }
  const drop_down_select = `<div class="dropDownMsg"><select class="browser-default dropDownSelect"> <option value="" disabled selected>Choose your option</option>${drop_down_options}</select></div>`;
  $(".chats").append(drop_down_select);
  scrollToBottomOfResults();
  
  $("select").on("change", function () {
    let value = "";
    let label = "";
    $("select option:selected").each(() => {
      label += $(this).val();
      value += $(this).val();
    });

    setUserResponse(label);
   
    send(value);
    $(".dropDownMsg").remove();
  });
}


function getUserPosition(position) {
  
  const response = `/inform{"latitude":${position.coords.latitude},"longitude":${position.coords.longitude}}`;
  $("#userInput").prop("disabled", false);

  send(response);
  showBotTyping();
}

function handleLocationAccessError(error) {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      console.log("User denied the request for Geolocation.");
      break;
    case error.POSITION_UNAVAILABLE:
      console.log("Location information is unavailable.");
      break;
    case error.TIMEOUT:
      console.log("The request to get user location timed out.");
      break;
    case error.UNKNOWN_ERROR:
      console.log("An unknown error occurred.");
      break;
    default:
      break;
  }

  const response = '/inform{"user_location":"deny"}';
 
  send(response);
  showBotTyping();
  $(".usrInput").val("");
  $("#userInput").prop("disabled", false);
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      getUserPosition,
      handleLocationAccessError
    );
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
}


function createCollapsible(collapsible_data) {
  // sample data format:
  // var collapsible_data=[{"title":"abc","description":"xyz"},{"title":"pqr","description":"jkl"}]
  let collapsible_list = "";
  for (let i = 0; i < collapsible_data.length; i += 1) {
    const collapsible_item = `<li><div class="collapsible-header">${collapsible_data[i].title}</div><div class="collapsible-body">
<span>${collapsible_data[i].description}</span></div></li>`;

    collapsible_list += collapsible_item;
  }
  const collapsible_contents = `<ul class="collapsible">${collapsible_list}</ul>`;
  $(collapsible_contents).appendTo(".chats");

  $(".collapsible").collapsible();
  scrollToBottomOfResults();
}


function createChart(
  title,
  labels,
  backgroundColor,
  chartsData,
  chartType,
  displayLegend
) {
  const html =
    '<div class="chart-container"> <span class="modal-trigger" id="expand" title="expand" href="#modal1"><i class="fa fa-external-link" aria-hidden="true"></i></span> <canvas id="chat-chart" ></canvas> </div> <div class="clearfix"></div>';
  $(html).appendTo(".chats");

  
  const ctx = $("#chat-chart");

  
  const data = {
    labels,
    datasets: [
      {
        label: title,
        backgroundColor,
        data: chartsData,
        fill: false,
      },
    ],
  };
  const options = {
    title: {
      display: true,
      text: title,
    },
    layout: {
      padding: {
        left: 5,
        right: 0,
        top: 0,
        bottom: 0,
      },
    },
    legend: {
      display: displayLegend,
      position: "right",
      labels: {
        boxWidth: 5,
        fontSize: 10,
      },
    },
  };

  chatChart = new Chart(ctx, {
    type: chartType,
    data,
    options,
  });

  scrollToBottomOfResults();
}


function createChartinModal(
  title,
  labels,
  backgroundColor,
  chartsData,
  chartType,
  displayLegend
) {
  // create the context that will draw the charts
  // over the canvas in the `#modal-chart` div of the modal
  const ctx = $("#modal-chart");

  // Once you have the element or context, instantiate the chart-type by passing the configuration,
  // for more info. refer: https://www.chartjs.org/docs/latest/configuration/
  const data = {
    labels,
    datasets: [
      {
        label: title,
        backgroundColor,
        data: chartsData,
        fill: false,
      },
    ],
  };
  const options = {
    title: {
      display: true,
      text: title,
    },
    layout: {
      padding: {
        left: 5,
        right: 0,
        top: 0,
        bottom: 0,
      },
    },
    legend: {
      display: displayLegend,
      position: "right",
    },
  };

  // eslint-disable-next-line no-undef
  modalChart = new Chart(ctx, {
    type: chartType,
    data,
    options,
  });
}


function setBotResponse(response) {
  setTimeout(() => {
    hideBotTyping();
    if (response.length < 1) {
      const fallbackMsg = "I am facing some issues, please try again later!!!";

      const BotResponse = `<img class="botAvatar" src="{% static 'images/sara_avatar.png' %}" /><p class="botMsg">${fallbackMsg}</p><div class="clearfix"></div>`;

      $(BotResponse).appendTo(".chats").hide().fadeIn(1000);
      scrollToBottomOfResults();
    } else {
      for (let i = 0; i < response.length; i += 1) {
        if (Object.hasOwnProperty.call(response[i], "text")) {
          if (response[i].text != null) {
            const BotResponse = `<img class="botAvatar" src="{% static 'images/sara_avatar.png' %}"  /><p class="botMsg">${response[i].text.replace(/(?:\r\n|\r|\n)/g, '<br>')}</p><div class="clearfix"></div>`;
            $(BotResponse).appendTo(".chats").hide().fadeIn(1000);
          }
        }
        if (Object.hasOwnProperty.call(response[i], "image")) {
          if (response[i].image !== null) {
            const BotResponse = `<div class="singleCard"><img class="imgcard" src="${response[i].image}"></div><div class="clearfix">`;

            $(BotResponse).appendTo(".chats").hide().fadeIn(1000);
          }
        }
        if (Object.hasOwnProperty.call(response[i], "buttons")) {
          if (response[i].buttons.length > 0) {
            addSuggestion(response[i].buttons);
          }
        }
        if (Object.hasOwnProperty.call(response[i], "attachment")) {
          if (response[i].attachment != null) {
            if (response[i].attachment.type === "video") {
              const video_url = response[i].attachment.payload.src;

              const BotResponse = `<div class="video-container"> <iframe src="${video_url}" frameborder="0" allowfullscreen></iframe> </div>`;
              $(BotResponse).appendTo(".chats").hide().fadeIn(1000);
            }
          }
        }
        if (Object.hasOwnProperty.call(response[i], "custom")) {
          const { payload } = response[i].custom;
          if (payload === "quickReplies") {
            const quickRepliesData = response[i].custom.data;
            showQuickReplies(quickRepliesData);
            return;
          }
          if (payload === "pdf_attachment") {
            renderPdfAttachment(response[i]);
            return;
          }
          if (payload === "dropDown") {
            const dropDownData = response[i].custom.data;
            renderDropDwon(dropDownData);
            return;
          }
          if (payload === "location") {
            $("#userInput").prop("disabled", true);
            getLocation();
            scrollToBottomOfResults();
            return;
          }
          if (payload === "cardsCarousel") {
            const restaurantsData = response[i].custom.data;
            showCardsCarousel(restaurantsData);
            return;
          }

          
          if (payload === "chart") {
            

            const chartData = response[i].custom.data;
            const {
              title,
              labels,
              backgroundColor,
              chartsData,
              chartType,
              displayLegend,
            } = chartData;

            
            createChart(
              title,
              labels,
              backgroundColor,
              chartsData,
              chartType,
              displayLegend
            );

            
            $(document).on("click", "#expand", () => {
              createChartinModal(
                title,
                labels,
                backgroundColor,
                chartsData,
                chartType,
                displayLegend
              );
            });
            return;
          }

          
          if (payload === "collapsible") {
            const { data } = response[i].custom;
            
            createCollapsible(data);
          }
        }
      }
      scrollToBottomOfResults();
    }
  }, 500);
}


function actionTrigger() {
  $.ajax({
    url: `http://localhost:5005/conversations/${sender_id}/execute`,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      name: action_name,
      policy: "MappingPolicy",
      confidence: "0.98",
    }),
    success(botResponse, status) {
      console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);

      if (Object.hasOwnProperty.call(botResponse, "messages")) {
        setBotResponse(botResponse.messages);
      }
      $("#userInput").prop("disabled", false);
    },
    error(xhr, textStatus) {
      // if there is no response from rasa server
      setBotResponse("");
      console.log("Error from bot end: ", textStatus);
      $("#userInput").prop("disabled", false);
    },
  });
}


function customActionTrigger() {
  $.ajax({
    url: "http://localhost:5055/webhook/",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      next_action: action_name,
      tracker: {
        sender_id,
      },
    }),
    success(botResponse, status) {
      console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);

      if (Object.hasOwnProperty.call(botResponse, "responses")) {
        setBotResponse(botResponse.responses);
      }
      $("#userInput").prop("disabled", false);
    },
    error(xhr, textStatus) {
      // if there is no response from rasa server
      setBotResponse("");
      console.log("Error from bot end: ", textStatus);
      $("#userInput").prop("disabled", false);
    },
  });
}


function send(message) {
  $.ajax({
    url: rasa_server_url,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ message, sender: sender_id }),
    success(botResponse, status) {
      console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);

      
      if (message.toLowerCase() === "/restart") {
        $("#userInput").prop("disabled", false);

        return;
      }
      setBotResponse(botResponse);
    },
    error(xhr, textStatus) {
      if (message.toLowerCase() === "/restart") {
        $("#userInput").prop("disabled", false);
       
      }

      setBotResponse("");
      console.log("Error from bot end: ", textStatus);
    },
  });
}


function restartConversation() {
  $("#userInput").prop("disabled", true);
  
  $(".collapsible").remove();

  if (typeof chatChart !== "undefined") {
    chatChart.destroy();
  }

  $(".chart-container").remove();
  if (typeof modalChart !== "undefined") {
    modalChart.destroy();
  }
  $(".chats").html("");
  $(".usrInput").val("");
  send("/restart");
}


$("#restart").click(() => {
  restartConversation();
});


$(".usrInput").on("keyup keypress", (e) => {
  const keyCode = e.keyCode || e.which;

  const text = $(".usrInput").val();
  if (keyCode === 13) {
    if (text === "" || $.trim(text) === "") {
      e.preventDefault();
      return false;
    }
    
    $(".collapsible").remove();
    $(".dropDownMsg").remove();
    if (typeof chatChart !== "undefined") {
      chatChart.destroy();
    }

    $(".chart-container").remove();
    if (typeof modalChart !== "undefined") {
      modalChart.destroy();
    }

    $("#paginated_cards").remove();
    $(".suggestions").remove();
    $(".quickReplies").remove();
    $(".usrInput").blur();
    setUserResponse(text);
    send(text);
    e.preventDefault();
    return false;
  }
  return true;
});

$("#sendButton").on("click", (e) => {
  const text = $(".usrInput").val();
  if (text === "" || $.trim(text) === "") {
    e.preventDefault();
    return false;
  }
  // destroy the existing chart
  if (typeof chatChart !== "undefined") {
    chatChart.destroy();
  }

  $(".chart-container").remove();
  if (typeof modalChart !== "undefined") {
    modalChart.destroy();
  }

  $(".suggestions").remove();
  $("#paginated_cards").remove();
  $(".quickReplies").remove();
  $(".usrInput").blur();
  $(".dropDownMsg").remove();
  setUserResponse(text);
  send(text);
  e.preventDefault();
  return false;
});


$("#profile_div").click(() => {
  $(".profile_div").toggle();
  $(".widget").toggle();
});


$(document).on("click", ".menu .menuChips", function () {
  const text = this.innerText;
  const payload = this.getAttribute("data-payload");
  console.log("payload: ", this.getAttribute("data-payload"));
  setUserResponse(text);
  send(payload);


  $(".suggestions").remove();
});


$("#clear").click(() => {
  $(".chats").fadeOut("normal", () => {
    $(".chats").html("");
    $(".chats").fadeIn();
  });
});


$("#close").click(() => {
  $(".profile_div").toggle();
  $(".widget").toggle();
  scrollToBottomOfResults();
});


$(document).on("click", ".quickReplies .chip", function () {
  const text = this.innerText;
  const payload = this.getAttribute("data-payload");
  console.log("chip payload: ", this.getAttribute("data-payload"));
  setUserResponse(text);
  send(payload);

  // delete the quickreplies
  $(".quickReplies").remove();
});