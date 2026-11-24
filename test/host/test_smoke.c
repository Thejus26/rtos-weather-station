/*
 * TEMPORARY harness smoke test (task s0-t4).
 *
 * Proves that `make test` runs a passing test (exit 0) and stops on a failing
 * assert() (non-zero exit). It does not touch components/app_logic/.
 * Deleted in task s1-t18-full-suite-run.
 */
#include <assert.h>

int main(void)
{
    assert(1 + 1 == 2);
    return 0;
}
