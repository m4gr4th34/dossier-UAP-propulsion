#!/usr/bin/env python3
"""
verify_numbers.py — executable checks for dossier-UAP-propulsion

    SECTION 1 / TRACK A — "Within known physics"  (PRE-RELEASE WORKING DRAFT)

Track A is CONDITIONAL: it takes the high-end kinematics *as reported* (with their
stated range/measurement assumptions) and asks what known physics then permits or
forbids. These checks verify the physics formulas for stated inputs — NOT that any
object actually moved this way. Each id matches the readable ledger (ledger.html)
and the checkable-claim tags in paper.html.

Sources pinned clean: Knuth, Powell & Reali, Entropy 21(10):939 (2019);
Loeb & Kirkpatrick, "Physical Constraints on UAP" (2023, draft) eqs (1)-(2).

No reliability claim is asserted; this is a single instrumented demonstration.
CI runs this on every push (.github/workflows/verify.yml). Fix the paper, never
widen a tolerance.
"""

import sys

PASS, FAIL = "PASS", "FAIL"
results = []


def check(label, computed, lo, hi, fmt="{:.4g}"):
    ok = lo <= computed <= hi
    status = PASS if ok else FAIL
    results.append((status, label, computed, (lo, hi)))
    print(f"[{status}] {'✓' if ok else '✗'} {label}")
    print(f"       computed={fmt.format(computed)}  claimed=[{fmt.format(lo)}, {fmt.format(hi)}]")
    return ok


print("=" * 72)
print("VERIFICATION — UAP propulsion, Section 1 / Track A (within known physics)")
print("CONDITIONAL on reported kinematics · PRE-RELEASE WORKING DRAFT")
print("=" * 72)

# Reported high-end ("radar") Tic Tac kinematics, as stated by Knuth et al. 2019:
#   28,000 ft -> sea level in 0.78 s; peak speed ~46,000 mph; energy ~4.3e11 J
#   at assumed mass 1000 kg; most-probable acceleration ~5370 g (lower bound).
V_PEAK_KMS = 20.6        # ~46,000 mph in km/s (as reported)
E_TICTAC_J = 4.3e11      # J, as reported (m = 1000 kg)
J_PER_TON_TNT = 4.184e9  # J per ton of TNT (definition)

# A01 — energy-to-TNT conversion of Knuth's stated drop energy.
tnt_tons = E_TICTAC_J / J_PER_TON_TNT
check("A01 Knuth Tic Tac energy 4.3e11 J equals ~100 tons TNT (as reported)",
      tnt_tons, 98.0, 108.0)

# A02 — Loeb-Kirkpatrick eq (2): optical fireball luminosity that KNOWN PHYSICS
#       requires for an object at the reported speed.
#   L_opt ~ 150 GW * (A/10 m^2) * (rho/0.3 kg m^-3) * (v/10 km s^-1)^3
A_M2 = 10.0        # frontal area, LK normalization (Tic Tac ~ tens of m^2)
RHO_KGM3 = 1.225   # ambient air density near sea level (drop ends at sea level)
L_opt_GW = 150.0 * (A_M2 / 10.0) * (RHO_KGM3 / 0.3) * (V_PEAK_KMS / 10.0) ** 3
check("A02 LK eq(2) predicted optical fireball ~5.3 TW (=5300 GW) at reported v",
      L_opt_GW, 5100.0, 5600.0)

# A03 — Mach number at the reported peak speed (c_sound ~ 343 m/s near sea level).
#       Hypersonic flight requires a strong shock, sonic boom, and thermal signature.
C_SOUND_MS = 343.0
mach = (V_PEAK_KMS * 1000.0) / C_SOUND_MS
check("A03 Mach number at reported peak speed (~Mach 60; shock+boom required)",
      mach, 57.0, 63.0)

# A04 — range sensitivity: LK fireball luminosity ~ distance^5, inferred v ~ distance.
#       A modest range error therefore swings the inferred 'anomaly' enormously.
range_error_factor = 3.0
luminosity_swing = range_error_factor ** 5    # distance^5 scaling
check("A04 a 3x range error swings inferred fireball luminosity by 3^5 = 243x",
      luminosity_swing, 243.0 - 1e-6, 243.0 + 1e-6)

# ----------------------------------------------------------------------
print()
n_fail = sum(1 for r in results if r[0] == FAIL)
n_pass = sum(1 for r in results if r[0] == PASS)
print("=" * 72)
print(f"TOTAL: {len(results)} checks · {n_pass} pass · {n_fail} fail")
print("All checks pass — Track A numbers reproduce." if not n_fail
      else "FAILURES FOUND — fix the paper, not the tolerances.")
print("=" * 72)
sys.exit(1 if n_fail else 0)
