/* Boot banner only. Tasks, queues and drivers arrive in later sprints. */
#include "esp_log.h"
#include "esp_system.h"

static const char *TAG = "main";

void app_main(void)
{
    ESP_LOGI(TAG, "RTOS weather station booting, IDF %s", esp_get_idf_version());
}
